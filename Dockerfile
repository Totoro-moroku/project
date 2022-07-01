FROM python:3.9.7-slim-buster

WORKDIR /app

COPY . /app


RUN pip install --upgrade pip

RUN pip install Flask

RUN pip install -U PyMySQL

CMD ["python3","index.py"]