FROM ubuntu:18.04

# 1.update
RUN apt-get -y update && apt-get -y upgrade

# 2.install basic packages
RUN apt-get install -y sudo wget bzip2
RUN apt-get install vim -y
RUN apt-get install -y git build-essential cmake clang libssl-dev

# 3.install python, pip
RUN apt-get install -y python3 python3-pip

# 4.set lang
RUN apt-get install locales locales-all
RUN export LANG=en_US.UTF-8
RUN locale-gen en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8

# 5.install library
RUN pip3 install econml
RUN pip3 install jupyterlab
RUN sudo apt-get install graphviz -y

# 6.create working dir
WORKDIR /
RUN mkdir /work
RUN cd /work 
RUN git clone https://github.com/microsoft/EconML.git

# 7.entrypoint
ENTRYPOINT ["jupyter", "lab","--ip=0.0.0.0","--allow-root", "--LabApp.token=''"]