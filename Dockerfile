FROM python:3

ENV TZ=Asia/Bangkok

WORKDIR /connect

COPY . /connect

RUN apt update
RUN apt install -y tmux
RUN pip install pytest-playwright
RUN pip install python-dotenv
RUN playwright install
RUN playwright install-deps

# docker build --platform linux/amd64 -t suphasan40/connect_kku_internet:amd64 .
# docker push suphasan40/connect_kku_internet:amd64