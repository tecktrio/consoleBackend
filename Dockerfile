FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /code

ADD . /code

COPY requirements.txt /code/requirements.txt

RUN pip install -r requirements.txt

COPY . /code
