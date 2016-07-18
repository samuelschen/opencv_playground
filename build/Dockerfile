FROM ubuntu:latest
MAINTAINER Jimmy Lee "jimmy.m.lee@gmail.com"

ARG OPENCV_VERISON="3.1.0"

# install dependencies
RUN apt-get update
RUN apt-get install -y libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev 
RUN apt-get install -y python-dev python-numpy python-scipy
RUN apt-get install -y python3-dev python3-numpy python3-scipy
RUN apt-get install -y curl build-essential checkinstall cmake 

# download opencv
RUN curl -sL https://github.com/Itseez/opencv/archive/$OPENCV_VERISON.tar.gz | tar xvz -C /tmp
RUN mkdir -p /tmp/opencv-$OPENCV_VERISON/build

WORKDIR /tmp/opencv-$OPENCV_VERISON/build

# install
RUN cmake -DWITH_FFMPEG=OFF -DWITH_OPENEXR=OFF -DWITH_CUDA=OFF -DWITH_NVCUVID=OFF ..
RUN make
RUN make install

# configure
RUN echo "/usr/local/lib" > /etc/ld.so.conf.d/opencv.conf
RUN ldconfig
RUN ln /dev/null /dev/raw1394

# cleanup package manager
RUN apt-get remove --purge -y curl build-essential checkinstall cmake
RUN apt-get autoclean && apt-get clean
RUN apt-get autoremove -y
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN rm -rf /var/lib/{apt,dpkg,cache,log}/

# prepare dir
RUN mkdir /source

VOLUME ["/source"]
WORKDIR /source
CMD ["bash"]