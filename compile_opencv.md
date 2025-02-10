## Compile opencv from source ( without lib... in ffmpeg, with gstreamer)

### When compiling opencv from source one may face missing dependency issues. Follow these steps first 
1. Before running cmake command always clear build directory if already tried compiling, 
    > cd build;rm -rf *;cmake .....

### Guidelines on installation
#### Make sure
    - path is correct here. OPENCV_EXTRA_MODULES_PATH=~/mywerks/opencv_build/opencv_contrib/modules<br>
    - sudo add-apt-repository universe<br>
    - sudo add-apt-repository multiverse<br>
    - sudo apt update

```
     ##### History 

   
      21  sudo dpkg -i libdc1394-25_2.2.6-4_amd64.deb 
      22  sudo apt -f install
      23  ll
      24  sudo dpkg -i libdc1394-dev_2.2.6-4_amd64.deb 
      25  sudo apt -f install
      26  ll
      27  sudo dpkg -i libdc1394-utils_2.2.6-4_amd64.deb 
      28  sudo apt -f install
      29  sudo apt install -y build-essential cmake git pkg-config libgtk-3-dev     libavcodec-dev libavformat-dev libswscale-dev libv4l-dev     libxvidcore-dev libx264-dev libjpeg-dev libpng-dev libtiff-dev     gfortran openexr libatlas-base-dev python3-dev python3-numpy     libtbb2 libtbb-dev
      30  sudo apt install -y libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev     gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-libav gstreamer1.0-plugins-bad     gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly
   
   
      36  mkdir opencv_build && cd opencv_build
      37  git clone --depth=1 https://github.com/opencv/opencv.git
      38  git clone --depth=1 https://github.com/opencv/opencv_contrib.git
      39  cd ~/opencv_build/opencv
      63  sudo apt install -y libopenblas-dev
      64  ldconfig -p | grep openblas
      65  sudo apt install -y libatlas-base-dev
      72  sudo apt update
      73  sudo apt install -y default-jdk
      74  java -version
      75  javac -version
      76  export JAVA_HOME=$(dirname $(dirname $(readlink -f $(which javac))))
      77  export PATH=$JAVA_HOME/bin:$PATH
      85  sudo apt update
      86  sudo apt install -y libavif-dev
      87  sudo apt install -y libopenblas-dev
      88  ldconfig -p | grep openblas
      89  sudo apt install -y libatlas-base-dev
      95  sudo apt install pyline
      96  sudo apt install pylint
      97  pylint --version
      98  sudo apt install flake8
      99  flake8 --version
     100  ll
     101  $ ~/.../build>rm -rf *
     103  cmake -D CMAKE_BUILD_TYPE=Release       -D CMAKE_INSTALL_PREFIX=/usr/local       -D OPENCV_EXTRA_MODULES_PATH=~/mywerks/opencv_build/opencv_contrib/modules       -D WITH_GSTREAMER=ON       -D WITH_FFMPEG=ON       -D WITH_V4L=ON       -D WITH_TBB=ON       -D WITH_OPENGL=ON ..
```


#### universe


#### cmake without ffmpeg with gstreamer
>    Update the GPG keyring with sudo apt-key adv.
     Manually enable the universe repository by editing /etc/apt/sources.list.
     Update your package list with sudo apt update.
     Install GStreamer using the apt command.


#### install opencv-contrib and have cmake point to it correctly


#### install ATLAS or OpenBLAS

✅ Recommended: Use OpenBLAS (libopenblas-dev) instead of ATLAS.
✅ Alternative: Install ATLAS (libatlas-base-dev) if required.
✅ Remove old build files and rerun CMake with -D WITH_LAPACK=ON.

##### history of commands