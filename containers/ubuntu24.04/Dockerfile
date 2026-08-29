FROM ubuntu:24.04

RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install gcc g++ clang clangd vim cmake software-properties-common git-all \
  python3 python3-pip python3-venv python3-antlr4 openjdk-21-jre-headless openjdk-21-jdk-headless -y && \
  apt autoremove -y && \
  apt clean -y

CMD ["bash", "start.sh", "-D"]
