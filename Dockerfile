FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt update
RUN apt install -y software-properties-common libssl-dev wget curl python3-pip vim

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -y unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99

RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1

RUN mkdir -p /src
COPY scrape.py /src/
COPY scrape.sh /src/
COPY requirements.txt /src/

WORKDIR /src
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD [ "./scrape.sh" ]
