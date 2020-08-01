FROM python:3.6-alpine

COPY ./requirements.txt /app/requirements.txt

COPY ./rocket_league.py /app/rocket_league.py

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD python rocket_league.py
