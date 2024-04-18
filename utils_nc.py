""" this is the code to convert the netCDF as geotiff for dbseabed"""

import xarray
import numpy as np

# load data
nc_data = xarray.open_dataset('./nc_files/gomex_allParams.nc')
nc_data.close()

# write crs
nc_data.rio.write_crs("epsg:4326", inplace=True)

# rename dimension and add dimension lat, lon
# the origial file bounding box is for corner value not for node value.
# so the lower left corner -98, 18 and lower left point -97.5, 18.05
nc_data = nc_data.rename_dims({'dimJ': 'y', 'dimI': 'x'})
nc_data.coords['y'] = np.arange(30.95, 17.95, -0.1)
nc_data.coords['x'] = np.arange(-97.95, -80.05, 0.1)

# write geotiff
nc_data['mud_pcnt'].rio.to_raster('./output/mud.tif')
nc_data['carbonate_pcnt'].rio.to_raster('./output/carbonate.tif')
