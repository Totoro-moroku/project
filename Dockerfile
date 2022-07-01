FROM python:3.9.7-slim-buster

WORKDIR /app

COPY . /app


RUN pip install --upgrade pip

RUN pip install Flask==2.0.3
RUN pip install graphene==2.1.6
RUN pip install Flask-GraphQL==2.0.0
RUN pip install PyMySQL


CMD ["python3","index.py"]