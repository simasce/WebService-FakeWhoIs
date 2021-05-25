FROM python:3.10.0a6-buster

EXPOSE 5000

WORKDIR /app

COPY /app /app/
COPY /static /app/static/

RUN pip install -r requirements.txt

WORKDIR /devapp

CMD ["python3","-u","app.py"]
