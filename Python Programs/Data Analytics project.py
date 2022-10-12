# This script downloads and plots monthly mean co2 values from https://datahub.io/core/co2-ppm#data

import os
import urllib.request
import pandas as pd
import matplotlib.pyplot as plt

# Check current directory and create new directory
cwd = os.getcwd()
print("Current working directory: %s" % cwd)
path = os.path.join(cwd,"Magic_Data")
if not os.path.isdir(path):
    os.mkdir(path)
    print("Newly created directory to store files: %s" % path)

# Provide the file path for the download. File path includes both the folder path and the file name
full_path = os.path.join(path,"co2-mm-mlo.csv")

# Download the file
print("Downloading file..........")
urllib.request.urlretrieve("https://datahub.io/core/co2-ppm/r/co2-mm-mlo.csv", full_path)
print("\n")
print("File has been downloaded!")

# Basic plotting
print("Performing super difficult data analysis..........")
fn = "co2-mm-mlo.csv"
carbon_dioxide = pd.read_csv(os.path.join(path,fn))
plt.plot(carbon_dioxide['Date'],carbon_dioxide['Average'])
plt.xlabel('Time')
plt.ylabel('CO2 concentration in ppm')
plt.show()
