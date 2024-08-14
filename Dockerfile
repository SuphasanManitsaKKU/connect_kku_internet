FROM python:3

ENV TZ=Asia/Bangkok

WORKDIR /connect

COPY . /connect

RUN apt update
RUN apt install -y tmux

# docker build --platform linux/amd64 -t suphasan40/connect_kku_internet:amd64 .
# docker push suphasan40/connect_kku_internet:amd64