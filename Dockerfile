FROM alpine:latest

RUN apk -U update --no-cache && \
    apk -U add --no-cache py3-pip && \
    adduser --system mtbaboard

ADD . /app

WORKDIR /app

RUN pip install --no-cache -r requirements.txt

EXPOSE 5000
CMD python -m flask run