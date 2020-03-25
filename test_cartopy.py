import os
import matplotlib.pyplot as plt
from netCDF4 import Dataset as netcdf_dataset

import cartopy.crs as ccrs

DIRBIN = os.path.dirname(os.path.abspath(__file__))

infile = os.path.join(
        DIRBIN,
        "b.e11.BRCP85C5CNBDRD.f09_g16.021.cice.h.hi_nh.208101-210012.nc"
        )

dataset = netcdf_dataset(infile)
sst = dataset.variables['hi'][0, :, :]
lats = dataset.variables['TLAT'][:]
lons = dataset.variables['TLON'][:]

ax = plt.axes(projection=ccrs.PlateCarree())

plt.contourf(lons, lats, sst, 60,
             transform=ccrs.PlateCarree())

ax.coastlines()

plt.show()
