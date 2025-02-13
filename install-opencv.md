#### This should install the OpenCV package without Jasper, as it's the recommended method for modern OpenCV installations
#### commands
sudo add-apt-repository universe
sudo apt update
sudo apt install libopencv-dev # this install a list of packages as shown below


> The following additional packages will be installed:
  gdal-data ibverbs-providers libaec0 libarmadillo10 libarpack2 libavcodec-dev libavformat-dev libavutil-dev libblosc1 libcfitsio9 libcharls2 libdc1394-dev
  libdeflate-dev libdouble-conversion3 libevent-core-2.1-7 libevent-pthreads-2.1-7 libexif-dev libexif-doc libfabric1 libfreexl1 libfyba0 libgdal30 libgdcm-dev
  libgdcm3.0 libgeos-c1v5 libgeos3.10.2 libgeotiff5 libgl2ps1.4 libglew2.2 libgphoto2-dev libhdf4-0-alt libhdf5-103-1 libhdf5-hl-100 libhwloc-plugins libhwloc15
  libibverbs1 libilmbase-dev libjbig-dev libjpeg-dev libjpeg-turbo8-dev libjpeg8-dev libjsoncpp25 libkmlbase1 libkmldom1 libkmlengine1 liblept5 libminizip1
  libmysqlclient21 libnetcdf19 libodbc2 libodbcinst2 libogdi4.1 libopencv-calib3d-dev libopencv-calib3d4.5d libopencv-contrib-dev libopencv-contrib4.5d
  libopencv-core-dev libopencv-core4.5d libopencv-dnn-dev libopencv-dnn4.5d libopencv-features2d-dev libopencv-features2d4.5d libopencv-flann-dev
  libopencv-flann4.5d libopencv-highgui-dev libopencv-highgui4.5d libopencv-imgcodecs-dev libopencv-imgcodecs4.5d libopencv-imgproc-dev libopencv-imgproc4.5d
  libopencv-ml-dev libopencv-ml4.5d libopencv-objdetect-dev libopencv-objdetect4.5d libopencv-photo-dev libopencv-photo4.5d libopencv-shape-dev
  libopencv-shape4.5d libopencv-stitching-dev libopencv-stitching4.5d libopencv-superres-dev libopencv-superres4.5d libopencv-video-dev libopencv-video4.5d
  libopencv-videoio-dev libopencv-videoio4.5d libopencv-videostab-dev libopencv-videostab4.5d libopencv-viz-dev libopencv-viz4.5d libopencv4.5-java
  libopencv4.5d-jni libopenexr-dev libopenmpi3 libpmix2 libpng-dev libpng-tools libpq5 libproj22 libpsm-infinipath1 libpsm2-2 libqhull-r8.0 libraw1394-dev
  libraw1394-tools librdmacm1 librttopo1 libsocket++1 libspatialite7 libsuperlu5 libswresample-dev libswscale-dev libsz2 libtbb-dev libtbb12 libtbb2
  libtbbmalloc2 libtesseract4 libtiff-dev libtiffxx5 libtk8.6 libucx0 liburiparser1 libvtk9.1 libxerces-c3.2 mysql-common opencv-data proj-bin proj-data
  unixodbc-common
> 
> 
> 
> #### Finally found a way to install cv2 , answered in stackoverflow
> ##### clone repo
> git clone https://github.com/opencv/opencv.git
> 
> ##### create build directory
>   cd ~/opencv
    mkdir build
    cd build
> 
> 
> ##### configure
> cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local .. \
      -D PYTHON_INCLUDE_DIR=/usr/include/python3.6 \
      -D PYTHON_INCLUDE_DIR2=/usr/include/x86_64-linux-gnu/python3.6m \
      -D BUILD_NEW_PYTHON_SUPPORT=ON \
      -D BUILD_opencv_python3=ON \
      -D HAVE_opencv_python3=ON \
      -D INSTALL_PYTHON_EXAMPLES=ON \
      -D PYTHON3_EXECUTABLE=/usr/bin/python3.6 \
      -D PYTHON_DEFAULT_EXECUTABLE=/usr/bin/python3.6 \
      -D PYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.6m.so \
      -D PYTHON3_PACKAGES_PATH=/usr/lib/python3/dist-packages .. \
      -D PYTHON3_NUMPY_INCLUDE_DIRS=/home/user/.local/lib/python3.6/site-packages/numpy/core/include/
> 
> 
> ##### build
> make -j8
> 
> ##### install libraries
> 
> sudo make install
> 
> ##### test
> 
> python3
> import cv2
> 
> ##### Note: If you don't know the path to numpy for the PYTHON3_NUMPY_INCLUDE_DIRS parameter, you can find it by executing import numpy and then numpy.__file__ in a python3 shell.