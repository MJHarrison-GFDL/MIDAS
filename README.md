[![Build Status](https://travis-ci.org/mjharriso/MIDAS.svg?branch=master)](https://travis-ci.org/mjharriso/MIDAS)

# DESCRIPTION

 MIDAS (MIDAS Midas is Data Analysis Software)
 is a Python package primarily for processing
 gridded data stored in CF-compliant NetCDF/HDF5 format
 (http://cfconventions.org).

 * spatial interpolation between quadrilateral meshes
 * temporal interpolation between calendar dates (datetime)
 * conservative re-mapping in the vertical dimension using MOM6/ALE
 * spatial integration/averaging
 * temporal averaging (Datetime).

 MIDAS was first developed by Matthew Harrison as an employee of NOAA in the
 GFDL Oceans and Sea Ice Processes Group.

 This work is licensed under the Creative Commons
 Attribution-NonCommercial-ShareAlike 3.0 Unported License.
 To view a copy of this license, visit
 http://creativecommons.org/licenses/by-nc-sa/3.0/
 or send a letter to Creative Commons, 444 Castro Street,
 Suite 900, Mountain View, California, 94041, USA.

# CONDA INSTALL

1. Download and install miniconda

```
(wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh;./Miniconda3-latest-Linux-x86_64.sh)
```

or, alternatively full Anaconda

```
(wget https://repo.anaconda.com/archive/Anaconda3-5.1.0-Linux-x86_64.sh;./Anaconda3-5.1.0-Linux-x86_64.sh)
```

2. Update your existing shell to add conda to your path

```
source ~/.bashrc
```

3. Now update conda

```
conda update conda
```

4. Install libgfortran (if needed)

```
sudo apt-get install libgfortran-6-dev
```

5. Activate Conda and setup the default (root) environment

```
source activate
```

6. Build zlib/hdf5/libnetcdf/libnetcdff

For best results, build these libraries yourself - conda does not handle dependencies for linking c and c++ libraries to fortran APIs - consider yourself lucky if you can work with pre-compiled packages and associated libraries

```
conda install conda-build
git clone git@github.com:MJHarrison-GFDL/conda-recipes.git
(cd conda-recipes/zlib;conda build .;conda install --use-local zlib)
(cd conda-recipes/hdf5;conda build .;conda install --use-local hdf5)
(cd conda-recipes/libnetcdf;conda build .;conda install --use-local libnetcdf)
(cd conda-recipes/libnetcdff;conda build .;conda install --use-local libnetcdff)
```

7. Optionally install with mpich2 if you have root privileges

```
(sudo apt-get install libmpich2-dev)
```

Or else if you do not have root privileges

```
(wget http://www.mpich.org/static/downloads/3.2.1/mpich-3.2.1.tar.gz;cd Downloads;tar xvf mpich-3.2.1.tar.gz;cd mpich-?3.2.1;./configure --enable-sha\
red --prefix=$CONDA_PREFIX;make; make install)
```


8. install the netCDF4 python API

```
pip install netCDF4
```

9. Install MIDAS in the root environment (libraries present)

```
git clone git@github.com:mjharriso/MIDAS.git
(cd MIDAS;git checkout dev/py36;. build.sh)
```

**TROUBLESHOOTING**

if you have a problem with libmkl missing:

```
conda install nomkl numpy scipy scikit-learn numexpr
conda remove mkl mkl-service
```

missing libcomm_err.so.3 at runtime?

```
ln -s CONDA_PREFIX/pkgs/krb5-1.14.6-0/lib/libcom_err.so.3 $CONDA_PREFIX/lib/.
```


**EXAMPLES**

```
cd examples
source activate MIDAS
python contour_example.py # Fetches OpenDAP URL from NODC and plots with Matplotlib
python hinterp_example.py # fms/horiz_interp does bi-linear interpolation from the original
                 	  # 1-deg to a 5-deg grid with masking
python hist.py            # volume-weighted histogram of salinity in the Indian Ocean
python subtile.py         # use subtiling algorithm to calculate un-weighted
 	       		  # cell average bathymetry and roughness. Example along the Eastern US
source deactivate
```

**HOW TO OBTAIN DOCUMENTATION**

```
ipython
import midas.rectgrid as rectgrid
rectgrid.[Tab]   # complete listing of methods
rectgrid.quadmesh       # a generic rectangular grid description
				    # Can be read from a file or provided as
				    # 2-d lat/lon position arrays.
rectgrid.state?  # Description of state instance
rectgrid.state.state.[Tab] # available methods for state objects
rectgrid.state.volume_integral?  # integrate scalars over the domain
				     # in 'X','Y','Z','XY' or 'XYZ'
rectgrid.state?? # View the code
```

**MORE INFORMATION**

type

```
conda list
```

this returns your current environment which should look like this:

```
File Edit Options Buffers Tools Help
alabaster                 0.7.10           py36h306e16b_0  
anaconda                  custom           py36hbbc8b67_0  
anaconda-client           1.6.9                    py36_0  
anaconda-navigator        1.7.0                    py36_0  
anaconda-project          0.8.2            py36h44fb852_0  
asn1crypto                0.24.0                   py36_0  
astroid                   1.6.1                    py36_0  
astropy                   2.0.3            py36h14c3975_0  
attrs                     17.4.0                   py36_0  
babel                     2.5.3                    py36_0  
backports                 1.0              py36hfa02d7e_1  
backports.shutil_get_terminal_size 1.0.0            py36hfea85ff_2  
beautifulsoup4            4.6.0            py36h49b8c8c_1  
bitarray                  0.8.1            py36h14c3975_1  
bkcharts                  0.2              py36h735825a_0  
bleach                    2.1.2                    py36_0  
bokeh                     0.12.13          py36h2f9c1c0_0  
boto                      2.48.0           py36h6e4cd66_1  
bottleneck                1.2.1            py36haac1ea0_0  
bzip2                     1.0.6                h9a117a8_4  
ca-certificates           2018.4.16                     0    conda-forge
cairo                     1.14.12              h77bcde2_0  
certifi                   2018.4.16                py36_0    conda-forge
cffi                      1.11.4           py36h9745a5d_0  
chardet                   3.0.4            py36h0f667ec_1  
click                     6.7              py36h5253387_0  
cloudpickle               0.5.2                    py36_1  
clyent                    1.2.2            py36h7e57e65_1  
colorama                  0.3.9            py36h489cec4_0  
conda                     4.5.2                    py36_0    conda-forge
conda-build               3.4.1                    py36_0  
conda-env                 2.6.0                h36134e3_1  
conda-verify              2.0.0            py36h98955d8_0  
contextlib2               0.5.5            py36h6c84a62_0  
cryptography              2.1.4            py36hd09be54_0  
curl                      7.58.0               h84994c4_0  
cycler                    0.10.0           py36h93f1223_0  
cython                    0.27.3           py36h1860423_0  
cytoolz                   0.9.0            py36h14c3975_0  
dask                      0.16.1                   py36_0  
dask-core                 0.16.1                   py36_0  
datashape                 0.5.4            py36h3ad6b5c_0  
dbus                      1.12.2               hc3f9b76_1  
decorator                 4.2.1                    py36_0  
distributed               1.20.2                   py36_0  
docutils                  0.14             py36hb0f60f5_0  
entrypoints               0.2.3            py36h1aec115_2  
et_xmlfile                1.0.1            py36hd6bccc3_0  
expat                     2.2.5                he0dffb1_0  
fastcache                 1.0.2            py36h14c3975_2  
filelock                  2.0.13           py36h646ffb5_0  
flask                     0.12.2           py36hb24657c_0  
flask-cors                3.0.3            py36h2d857d3_0  
fontconfig                2.12.4               h88586e7_1  
freetype                  2.8                  hab7d2ae_1  
get_terminal_size         1.0.0                haa9412d_0  
gevent                    1.2.2            py36h2fe25dc_0  
glib                      2.53.6               h5d9569c_2  
glob2                     0.6              py36he249c77_0  
gmp                       6.1.2                h6c8ec71_1  
gmpy2                     2.0.8            py36hc8893dd_2  
graphite2                 1.3.10               hf63cedd_1  
greenlet                  0.4.12           py36h2d503a6_0  
gst-plugins-base          1.12.4               h33fb286_0  
gstreamer                 1.12.4               hb53b477_0  
harfbuzz                  1.7.4                hc5b324e_0  
hdf5                      1.8.20                        0    local
heapdict                  1.0.0                    py36_2  
html5lib                  1.0.1            py36h2f9c1c0_0  
icu                       58.2                 h9c2bf20_1  
idna                      2.6              py36h82fb2a8_1  
imageio                   2.2.0            py36he555465_0  
imagesize                 0.7.1            py36h52d8127_0  
intel-openmp              2018.0.0             hc7b2577_8  
ipykernel                 4.8.0                    py36_0  
ipython                   6.2.1            py36h88c514a_1  
ipython_genutils          0.2.0            py36hb52b0d5_0  
ipywidgets                7.1.1                    py36_0  
isort                     4.2.15           py36had401c0_0  
itsdangerous              0.24             py36h93cc618_1  
jbig                      2.1                  hdba287a_0  
jdcal                     1.3              py36h4c697fb_0  
jedi                      0.11.1                   py36_0  
jinja2                    2.10             py36ha16c418_0  
jpeg                      9b                   h024ee3a_2  
jsonschema                2.6.0            py36h006f8b5_0  
jupyter                   1.0.0                    py36_4  
jupyter_client            5.2.2                    py36_0  
jupyter_console           5.2.0            py36he59e554_1  
jupyter_core              4.4.0            py36h7c827e3_0  
jupyterlab                0.31.5                   py36_0  
jupyterlab_launcher       0.10.2                   py36_0  
lazy-object-proxy         1.3.1            py36h10fcdad_0  
libcurl                   7.58.0               h1ad7b7a_0  
libedit                   3.1                  heed3624_0  
libffi                    3.2.1                hd88cf55_4  
libgcc-ng                 7.2.0                h7cc24e2_2  
libgfortran-ng            7.2.0                h9f7466a_2  
libnetcdf                 4.4.1                         0    local
libnetcdff                4.4.4                         0    local
libpng                    1.6.34               hb9fc6fc_0  
libsodium                 1.0.15               hf101ebd_0  
libssh2                   1.8.0                h9cfc8f7_4  
libstdcxx-ng              7.2.0                h7a57d05_2  
libtiff                   4.0.9                h28f6b97_0  
libtool                   2.4.6                h544aabb_3  
libxcb                    1.12                 hcd93eb1_4  
libxml2                   2.9.7                h26e45fe_0  
libxslt                   1.1.32               h1312cb7_0  
llvmlite                  0.21.0           py36ha241eea_0  
locket                    0.2.0            py36h787c0ad_1  
lxml                      4.1.1            py36hf71bdeb_1  
lzo                       2.10                 h49e0be7_2  
markupsafe                1.0              py36hd9260cd_1  
matplotlib                2.1.2            py36h0e671d2_0  
mccabe                    0.6.1            py36h5ad9710_1  
midas                     1.2.4                     <pip>
midas                     1.2.5                     <pip>
mistune                   0.8.3                    py36_0  
mkl                       2018.0.1             h19d6760_4  
mkl-service               1.1.2            py36h17a0993_4  
mpc                       1.0.3                hec55b23_5  
mpfr                      3.1.5                h11a74b3_2  
mpmath                    1.0.0            py36hfeacd6b_2  
msgpack-python            0.5.1            py36h6bb024c_0  
multipledispatch          0.4.9            py36h41da3fb_0  
navigator-updater         0.1.0            py36h14770f7_0  
nbconvert                 5.3.1            py36hb41ffb7_0  
nbformat                  4.4.0            py36h31c9010_0  
ncurses                   6.0                  h9df7e31_2  
netCDF4                   1.3.1                     <pip>
networkx                  2.1                      py36_0  
nltk                      3.2.5            py36h7532b22_0  
nose                      1.3.7            py36hcdf7029_2  
notebook                  5.4.0                    py36_0  
numba                     0.36.2          np114py36hc6662d5_0  
numexpr                   2.6.4            py36hc4a3f9a_0  
numpy                     1.14.0           py36h3dfced4_1  
numpydoc                  0.7.0            py36h18f165f_0  
odo                       0.5.1            py36h90ed295_0  
olefile                   0.45.1                   py36_0  
openpyxl                  2.4.10                   py36_0  
openssl                   1.0.2o                        0    conda-forge
packaging                 16.8             py36ha668100_1  
pandas                    0.22.0           py36hf484d3e_0  
pandoc                    1.19.2.1             hea2e7c5_1  
pandocfilters             1.4.2            py36ha6701b7_1  
pango                     1.41.0               hd475d92_0  
parso                     0.1.1            py36h35f843b_0  
partd                     0.3.8            py36h36fd896_0  
patchelf                  0.9                  hf79760b_2  
path.py                   10.5             py36h55ceabb_0  
pathlib2                  2.3.0            py36h49efa8e_0  
patsy                     0.5.0                    py36_0  
pcre                      8.41                 hc27e229_1  
pep8                      1.7.1                    py36_0  
pexpect                   4.3.1                    py36_0  
pickleshare               0.7.4            py36h63277f8_0  
pillow                    5.0.0            py36h3deb7b8_0  
pip                       9.0.1            py36h6c6f9ce_4  
pixman                    0.34.0               hceecf20_3  
pkginfo                   1.4.1            py36h215d178_1  
pluggy                    0.6.0            py36hb689045_0  
ply                       3.10             py36hed35086_0  
prompt_toolkit            1.0.15           py36h17d85b1_0  
psutil                    5.4.3            py36h14c3975_0  
ptyprocess                0.5.2            py36h69acd42_0  
py                        1.5.2            py36h29bf505_0  
pycodestyle               2.3.1            py36hf609f19_0  
pycosat                   0.6.3            py36h0a5515d_0  
pycparser                 2.18             py36hf9f622e_1  
pycrypto                  2.6.1            py36h14c3975_7  
pycurl                    7.43.0.1         py36hb7f436b_0  
pyflakes                  1.6.0            py36h7bd6a15_0  
pygments                  2.2.0            py36h0d3125c_0  
pylint                    1.8.2                    py36_0  
pyodbc                    4.0.22           py36hf484d3e_0  
pyopenssl                 17.5.0           py36h20ba746_0  
pyparsing                 2.2.0            py36hee85983_1  
pyqt                      5.6.0            py36h0386399_5  
pysocks                   1.6.7            py36hd97a5b1_1  
pytest                    3.3.2                    py36_0  
python                    3.6.4                hc3d631a_1  
python-dateutil           2.6.1            py36h88d3b88_1  
pytz                      2017.3           py36h63b9c63_0  
pywavelets                0.5.2            py36he602eb0_0  
pyyaml                    3.12             py36hafb9ca4_1  
pyzmq                     16.0.3           py36he2533c7_0  
qt                        5.6.2               h974d657_12  
qtawesome                 0.4.4            py36h609ed8c_0  
qtconsole                 4.3.1            py36h8f73b5b_0  
qtpy                      1.3.1            py36h3691cc8_0  
readline                  7.0                  ha6073c6_4  
requests                  2.18.4           py36he2e5f8d_1  
rope                      0.10.7           py36h147e2ec_0  
ruamel_yaml               0.15.35          py36h14c3975_1  
scikit-image              0.13.1           py36h14c3975_1  
scikit-learn              0.19.1           py36h7aa7ec6_0  
scipy                     1.0.0            py36hbf646e7_0  
seaborn                   0.8.1            py36hfad7ec4_0  
send2trash                1.4.2                    py36_0  
setuptools                38.4.0                   py36_0  
simplegeneric             0.8.1                    py36_2  
singledispatch            3.4.0.3          py36h7a266c3_0  
sip                       4.18.1           py36h51ed4ed_2  
six                       1.11.0           py36h372c433_1  
snowballstemmer           1.2.1            py36h6febd40_0  
sortedcollections         0.5.3            py36h3c761f9_0  
sortedcontainers          1.5.9                    py36_0  
sphinx                    1.6.6                    py36_0  
sphinxcontrib             1.0              py36h6d0f590_1  
sphinxcontrib-websupport  1.0.1            py36hb5cb234_1  
spyder                    3.2.6                    py36_0  
sqlalchemy                1.2.1            py36h14c3975_0
sqlite                    3.22.0               h1bed415_0
statsmodels               0.8.0            py36h8533d0b_0
sympy                     1.1.1            py36hc6d1c1c_0
tblib                     1.3.2            py36h34cf8b6_0
terminado                 0.8.1                    py36_1
testpath                  0.3.1            py36h8cadb63_0
tk                        8.6.7                hc745277_3
toolz                     0.9.0                    py36_0
tornado                   4.5.3                    py36_0
traitlets                 4.3.2            py36h674d592_0
typing                    3.6.2            py36h7da032a_0
unicodecsv                0.14.1           py36ha668878_0
unixodbc                  2.3.4                hc36303a_1
urllib3                   1.22             py36hbe7ace6_0
wcwidth                   0.1.7            py36hdf4376a_0
webencodings              0.5.1            py36h800622e_1
werkzeug                  0.14.1                   py36_0
wheel                     0.30.0           py36hfd4bba0_1
widgetsnbextension        3.1.0                    py36_0
wrapt                     1.10.11          py36h28b7045_0
xlrd                      1.1.0            py36h1db9f0c_1
xlsxwriter                1.0.2            py36h3de1aca_0
xlwt                      1.3.0            py36h7b00a1f_0
xz                        5.2.3                h55aa19d_2
yaml                      0.1.7                had09818_2
zict                      0.1.3            py36h3a3bf81_0
zlib                      1.2.11                        1    local

```