FROM cjb873/leorover_image:1.0


RUN apt update \
&& sudo sh -c 'echo "deb http://files.fictionlab.pl/repo $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list' \
&& sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key B09817643168B68528DE78BDB070AF638C33109D \
&& sudo apt update && sudo apt -y upgrade \
&& sudo apt install -y ros-noetic-leo-examples \
&& sudo apt install -y ros-noetic-ar-track-alvar \
&& pip3 install tflite-runtime

RUN git clone https://github.com/DiscoverCCRI/RoverDemo.git \
&& mv RoverDemo/experiment_files ~/ && sudo rm -r RoverDemo

RUN echo "172.18.0.1 rover02" >> /etc/hosts
RUN rm /ros_entrypoint.sh
