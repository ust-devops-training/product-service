# Base image for ProductService

FROM python:3.7-slim

RUN apt-get update && \
    pip install --upgrade pip

ENV INSTALL_PATH /usr/src/app/
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH


RUN pwd

COPY . .
RUN pip install -r requirements.txt
ENV BIN_PATH $INSTALL_PATH/api

WORKDIR $BIN_PATH

CMD ["gunicorn", "--bind", "0.0.0.0:5001", "wsgi:app"]