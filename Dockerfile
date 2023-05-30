FROM python:latest

WORKDIR /code
COPY . /code/
RUN pip3 install -r requirments.txt