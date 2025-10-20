import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
url = "https://www.ngdc.noaa.gov/thredds/dodsC/regional/monterey_bay_P080_2018.nc"
ds = xr.open_dataset(url)

# Extract bathymetry variable
da = ds["Band1"]

# Mask null values 
arr = da.where(np.isfinite(da))

# Get coordinate bounds
lat_min = float(arr["lat"].min())
lat_max = float(arr["lat"].max())
lon_min = float(arr["lon"].min())
lon_max = float(arr["lon"].max())

print(f"Latitude range: {lat_min:.4f} to {lat_max:.4f}")
print(f"Longitude range: {lon_min:.4f} to {lon_max:.4f}")


# Plot the DEMs
plt.figure(figsize=(8, 6))
plt.pcolormesh(arr["lon"], arr["lat"], arr, shading="auto", cmap="viridis")
plt.colorbar(label="Elevation / Depth (m)")
plt.title("Monterey Bay - NCEI")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.tight_layout()
plt.show()
