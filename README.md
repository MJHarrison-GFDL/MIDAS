INSTALL
=======

                mkdir projects
                cd projects
                git clone git@github.com:mjharriso/MIDAS.git
                cd MIDAS
                mkdir fms_siena
                cd fms_siena
                cvs co -r testing bin site
                cvs co -r siena_201204 shared
                cvs update -r siena_20121201_mjh shared/horiz_interp/horiz_interp.F90
                cvs update -r siena_20121201_mjh shared/horiz_interp/horiz_interp_bilinear.F90
                cvs update -r siena_20121201_mjh site/hpcs/intel.mk
                cvs update -r siena_20121201_mjh shared/mpp/include/mpp_comm_nocomm.inc
                cvs update -r siena_20121201_mjh shared/mpp/include/mpp_do_update_nonblock.h
                cd ../fms_build
                ./build_fms.csh
                cd../hinterp
                ./build_hinterp.csh

add this to your .cshrc

                setenv PATH /net2/mjh/local/bin:/net2/mjh/local/python-2.7.3/bin:${PATH}
                setenv PYTHONPATH $HOME/projects/MIDAS
                setenv GEOS_DIR /net2/mjh/local


OR

add the following to your .cshrc:

                setenv PATH  /net2/mjh/local/bin:/net2/mjh/local/python-2.7.3/bin:${PATH}
                setenv PYTHONPATH /net2/mjh/projects
                setenv GEOS_DIR /net2/mjh/local




=== MIDAS Schematic Snapshot 12/01/2012 ===

                .state [(t),(s),y,x]              <--- Top level state
                   .supergrid[y,x]                   <---  Top level grid (FMS supergrid)
                      .grid[y,x]                        <---  Derived from supergrid (or externally)
                                                        <---  fms mom4,gold grids and supergrids
                                                        <---  can be imported
                   .variables                           <---  generic [(t),(s),y,x] fields
                        .interfaces[(t),s,y,x]          <---  Interfaces reside on a static grid but 
                                                        <---  vary in time at each interface                  
                        
                grid methods
                                .geo_region                     <--- Define a geographic region
                                .indexed_region                 <--- Define a indexed region
                                .extract                        <--- extract grid info to an indexed or geo region
                                .add_mask                       <--- Define a mask
                                

                state methods
                                .create_field                   <--- Create a new field from existing state variables
                                .add_field_from_array           <--- Use a array + dictionary to define a new state var
                                .del_field
                                .rename_field
                                .mask_field                     <--- Use grid mask 
                                .unmask
                                .mask_where
                                .add_interface_bounds           <--- Define interface positions at cell boundaries
                                .fill_interior                  <--- Fill masked points above topography
                                .volume_integral                <--- X,Y,XY,XYZ,... finite volume integrals
                                .time_avg                       <--- Time-weighted/Volume-weighted means
                                .monthly_avg                    <--- Time/Volume-weighted means for calendar months
                                .monthly_anom                   <--- Anomalies wrt monthly climatological values
                                .time_smooth                    <--- Window-weighted averages
                                .remap_Z_to_layers              <--- Convert from z to isopycnal
                                .adjust_thickness               <--- Use topography for tracers
                                .horiz_interp                   <--- 2-d interpolation via FMS horiz_interp
                                .grid_overlap_struct            <--- cell remapping (mean/max/min/std)
                                .eof                            <--- Computes Eigenvectors and Eigenvalues of covariance
                                .write_nc                       <--- Output NetCDF 
                                

=== Examples ====
                                

Read (z,y,x) annual mean temperature from NODA and plot surface values:
                
                from midas import *
                grid=generic_rectgrid('http://data.nodc.noaa.gov/thredds/dodsC/woa/WOA09/NetCDFdata/temperature_annual_1deg.nc',var='t_an',cyclic=True)
                State=state(grid=grid,path='http://data.nodc.noaa.gov/thredds/dodsC/woa/WOA09/NetCDFdata/temperature_annual_1deg.nc',fields=['t_an'])
                print State.variables                

                xax=State.grid.x_T
                yax=State.grid.y_T
                sout=sq(State.t_an[0,0,:])
                cf=plt.contourf(xax,yax,sout,np.arange(-2,31,1),extend='both')
                plt.colorbar(cf)
                plt.show()
                
    
Information can be readily read from the .state container and the user is able to modify its
contents directly. For example, attribute detection is a frequent point of failure for 
MIDAS routines.  The user can fix a known attribute problem, e.g.

                print state.var_dict['t_an']['Ztype']
                state.var_dict['t_an']['Ztype']='Fixed'
                
                
MIDAS state variables have several useful methods , e.g. volume integrals are
available for data on geopotential coordinate grids, s=s(z), or Lagrangian 
coordinate, s=s(x,y,z,t):

Read (z,y,x) annual temperature from NODC and calculate volume-weighted means
(skipping masked values over land):

                from midas import *
                grid=generic_rectgrid('http://data.nodc.noaa.gov/thredds/dodsC/woa/WOA09/NetCDFdata/temperature_annual_1deg.nc',var='t_an',cyclic=True)
                State=state(grid=grid,path='http://data.nodc.noaa.gov/thredds/dodsC/woa/WOA09/NetCDFdata/temperature_annual_1deg.nc',fields=['t_an'])
                State.volume_integral('t_an','XY',normalize=True)
                plt.plot(sq(S.t_an_xyav))
                plt.grid()
                plt.show()
                
                print State.variables
                print State.t_an_xyav
                State.volume_integral('t_an','XYZ',normalize=True)
                print State.t_an_xyzav
                
