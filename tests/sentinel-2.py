from pystac_client import Client
import stackstac
import rioxarray as rxr
import numpy as np
import os
import matplotlib.pyplot as plt
import numpy as np

# Latitudinal and longitudinal extents
bbox = (-122.030138899805, 36.599861085915, -121.779953721625, 36.980138853044984)

# Search for low cloud scene in date window
catalog = Client.open("https://earth-search.aws.element84.com/v1")
items = list(catalog.search(
    collections =["sentinel-2-l2a"],
    bbox = bbox,
    datetime = "2025-10-17/2025-10-18",
    query = {"eo:cloud_cover": {"lte": 20}},
    limit = 50
).items())

# If no items found, print result and exit
if not items:
    print(f"No items found")
    raise SystemExit("No Sentinel-2 scenes found for these filters.")

# If items found, print number of items
print(f"Found {len(items)} Sentinel-2 scenes")

# Pick the least-cloudy item
items.sort(key = lambda it: it.properties.get("eo:cloud_cover", 1000))
item = [items[2]]

# Print attributes of selected item
print("ID:", item[0].id)
print("Cloud cover:", item[0].properties.get("eo:cloud_cover"))
print("Datetime:", item[0].datetime)
print("Available assets:", list(item[0].assets.keys()))

# Load visual layer from dataset and open raster
vis_url = item[0].assets["visual"].href
vis = rxr.open_rasterio(vis_url) 
vis4326 = vis.rio.reproject(4326)
vis_clip = vis4326.rio.clip_box(*bbox) 

# Reorder to (y, x, band) and scale to 0 – 1
arr = vis_clip.transpose("y","x","band").values.astype("float32") / 255.0

plt.figure(figsize=(4,6))
plt.imshow(np.clip(arr, 0, 1))
plt.axis("off")
plt.title("Monterey Bay - Sentinel-2")
plt.show()
