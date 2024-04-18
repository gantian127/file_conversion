""" this is the code to convert the Esri ASCII as geotiff for dbseabed"""

import rioxarray
import os
import numpy as np


# get the folder path for raw ascii files
ascii_folder = "./ascii_files_totlsu"
output_folder = "./output_totlsu"


# loop each ascii file for conversion
for file_name in os.listdir(ascii_folder):

    if file_name.endswith(".asc"):
        # load data
        input_file_name = os.path.join(ascii_folder, file_name)
        esri_data = rioxarray.open_rasterio(input_file_name, mode='w+', **{'dtype': 'float64'})

        # write crs
        esri_data.rio.write_crs("epsg:4326", inplace=True)

        # convert float32 values as original float64 values from ascii file
        esri_data.data = esri_data.astype("float64")
        esri_float64_values = np.loadtxt(input_file_name, skiprows=6)
        esri_data.data[0] = esri_float64_values

        # write geotiff
        geotiff_name = f"{file_name[:-9]}.tif"
        esri_data.rio.to_raster(os.path.join(output_folder, geotiff_name),
                                dtype="float64", recalc_transform=False)

print("File conversion is done!")


