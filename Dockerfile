# syntax=docker/dockerfile:1
# File basically copied from:
# https://docs.docker.com/language/python/build-images/#create-a-dockerfile-for-python
# With some minimal modifications.

FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
