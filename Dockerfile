FROM ubuntu:latest

ENV TZ 'Europe/Berlin'

RUN echo $TZ > /etc/timezone 

RUN apt-get update \
    && apt-get install -y tzdata \
    && rm /etc/localtime \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata \
    && apt-get clean

RUN apt-get install --yes build-essential lsb-release curl sudo vim python3-pip apt-utils dos2unix git gh fdupes file

RUN echo "%user	ALL=(ALL:ALL) NOPASSWD:ALL" >/etc/sudoers.d/user
RUN echo "root:password" | chpasswd

#
# LaTex
#
RUN apt-get install --yes libcairo2-dev libpango1.0-dev ffmpeg
RUN apt-get install --yes texlive-latex-extra texlive-fonts-extra texlive-science

#
# User
#
RUN useradd -ms /bin/bash user

USER user
WORKDIR /home/user

RUN echo '\nPATH=$PATH:/$HOME/bin:$HOME/.local/bin' >>$HOME/.bashrc

#
# Manim
#
RUN pip3 install manim manimlib

#
CMD ["bash"]
