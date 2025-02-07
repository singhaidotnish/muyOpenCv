## Compile opencv from source ( without lib... in ffmpeg, with gstreamer)

### When compiling opencv from source one may face missing dependency issues. Follow these steps first 
1. Before running cmake command always clear build directory if already tried compiling, 
    > cd build;rm -rf *;cmake .....
2. 


#### universe


#### cmake without ffmpeg with gstreamer
>Update the GPG keyring with sudo apt-key adv.
Manually enable the universe repository by editing /etc/apt/sources.list.
Update your package list with sudo apt update.
Install GStreamer using the apt command.


#### install opencv-contrib and have cmake point to it correctly


#### install ATLAS or OpenBLAS

✅ Recommended: Use OpenBLAS (libopenblas-dev) instead of ATLAS.
✅ Alternative: Install ATLAS (libatlas-base-dev) if required.
✅ Remove old build files and rerun CMake with -D WITH_LAPACK=ON.

##### history of commands