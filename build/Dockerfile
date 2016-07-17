FROM ubuntu:latest
MAINTAINER Jimmy Lee "jimmy.m.lee@gmail.com"

ARG OPENCV_VERISON="3.1.0"

# install dependencies
RUN apt-get update
RUN apt-get install -y --fix-missing libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev 
RUN apt-get install -y --fix-missing python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
RUN apt-get install -y --fix-missing curl build-essential checkinstall cmake unzip

# download opencv
RUN curl -sL https://github.com/Itseez/opencv/archive/3.1.0.zip | unzip -d /tmp
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
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# prepare dir
RUN mkdir /source

VOLUME ["/source"]
WORKDIR /source
CMD ["bash"]