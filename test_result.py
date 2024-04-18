"""
This is used to test if the new file has the same value as the ori file
"""


import rioxarray
import os
import numpy as np


# get the folder path for raw ascii files
ascii_folder = "./ascii_files"
output_folder = "./output"

for file_name in os.listdir(ascii_folder):
    if file_name.endswith(".asc"):
        asc_file = os.path.join(ascii_folder, file_name)
        tif_file = os.path.join(output_folder, f"{file_name[:-9]}.tif")
        asc_data = np.loadtxt(asc_file, skiprows=6)
        tif_data = rioxarray.open_rasterio(tif_file)

        diff = tif_data[0] - asc_data
        if not np.all(diff == 0):
            print(f'wrong data for {tif_file}')
        else:
            print(diff.data.sum())
