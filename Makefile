SHELL=bash

all: MIDAS

MIDAS:	MOM6_ALE/build_ale/libale.a
	-rm -rf build/*
	python setup.py config_fc --f90flags="-i4 -r8 -DPY_SOLO" --fcompiler=gfortran \
	--f90flags="-fcray-pointer -fdefault-real-8 \
	-ffixed-line-length-132 -ffree-line-length-0 -DPY_SOLO" build
	python setup.py install


MOM6_ALE/build_ale/libale.a:
	(cd fms;tar xf fms_env.tar;cd ..;cd MOM6_ALE/build_ale;cp build_ale.csh tmp;\
 	  sed -e 's/#set platform = linux/set platform = linux/' < tmp > tmp2;\
	  sed -e 's/set platform = gfdl_hpcs/#set platform = gfdl_hpcs/' < tmp2 > build_ale.csh;\
	  chmod +x ./build_ale.csh;./build_ale.csh)
