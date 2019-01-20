FROM python:3-stretch

RUN mkdir -p /usr/app
ADD . /usr/app/
WORKDIR /usr/app

RUN pip install -r requirements.txt

CMD ./scripts/run-bot.sh
