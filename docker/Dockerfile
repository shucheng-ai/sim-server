FROM ubuntu:18.04
ENV DEBIAN_FRONTEND=noninteractive
ENV LANG C.UTF-8
USER root
ADD sources.list /etc/apt/sources.list
ADD pip.conf /root/.pip/pip.conf
RUN apt-get update
RUN apt-get install -y python3-pip libpython3-dev vim rsync
RUN pip3 install flask
