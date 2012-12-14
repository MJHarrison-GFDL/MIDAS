from midas import *



lon=np.arange(0,360,.5)
lat=np.arange(20.,65,.5)

X,Y=np.meshgrid(lon,lat)
grid=generic_rectgrid(lon=X,lat=Y,cyclic=False)

grid_obs=generic_rectgrid(path='http://data.nodc.noaa.gov/thredds/dodsC/woa/WOA09/NetCDFdata/temperature_annual_1deg.nc',var='t_an')

S=state(path='http://data.nodc.noaa.gov/thredds/dodsC/woa/WOA09/NetCDFdata/temperature_annual_1deg.nc',grid=grid_obs,geo_region=None,fields=['t_an'])
T=S.horiz_interp('t_an',target=grid,src_modulo=True,method=1) 
xax=T.grid.x_T
yax=T.grid.y_T
sout=np.squeeze(T.t_an[0,0,:])

fig=plt.figure(1)
cf=plt.contourf(xax,yax,sout,np.arange(-2,25,1),extend='both')
plt.colorbar(cf)
plt.grid()
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('SST from NODC WOA09')
plt.savefig('hinterp.png')
plt.show()
