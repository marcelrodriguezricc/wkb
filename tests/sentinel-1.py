import os, numpy as np, matplotlib.pyplot as plt
import rasterio
from pystac_client import Client

# AWS Anonymous Login
os.environ["AWS_NO_SIGN_REQUEST"] = "YES"
os.environ["AWS_REQUEST_PAYER"]   = "requester"

# Selected Sentinel-1 scene
scene_id = "S1A_IW_GRDH_1SDV_20251010T020743_20251010T020808_061357_07A800"

# Open dataset for scene
cat = Client.open("https://earth-search.aws.element84.com/v1")
it = next(cat.search(
    collections=["sentinel-1-grd"],
    ids=[scene_id]
).items())
href = it.assets.get("sigma0_vv", it.assets.get("vv")).href
print("Using:", href)

# Bounding box
col_start_ds, col_stop_ds = 1466, 1622
row_start_ds, row_stop_ds = 277, 719
scale = 10
col_start, col_stop = col_start_ds * scale, col_stop_ds * scale
row_start, row_stop = row_start_ds * scale, row_stop_ds * scale

# Generate raster
with rasterio.open(href) as src:
    window = rasterio.windows.Window.from_slices(
        (row_start, row_stop),
        (col_start, col_stop)
    )
    arr = src.read(1, window=window).astype("float32")


# Normalize and convert to dB
arr_norm = arr / np.nanmax(arr)
arr_db = 10 * np.log10(np.clip(arr_norm, 1e-6, None))

# Plot
plt.figure(figsize=(4, 8))
plt.imshow(arr_db, cmap="gray", vmin=-25, vmax=0, origin="upper")
plt.colorbar(label="σ⁰ VV (dB)")
plt.title(f"Monterey Bay - Sentinel-1")
plt.axis("off")
plt.tight_layout()
plt.show()
