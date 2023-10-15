FROM ubuntu:latest

RUN apt-get update
RUN apt-get -y upgrade

RUN apt-get -y install git
RUN apt-get -y install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
RUN apt-get -y install python2 python3 python3-pip
RUN apt-get -y install curl
RUN curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
RUN python2 get-pip.py
RUN rm get-pip.py
RUN pip2 install antlr4-python2-runtime
RUN pip3 install antlr4-python3-runtime
RUN apt-get -y install net-tools
RUN apt-get -y install default-jdk default-jre

RUN apt-get -y autoremove

RUN rm -rf /root/GOLD
RUN mkdir /root/GOLD

WORKDIR /root
