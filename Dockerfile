FROM python:3.10

RUN adduser --disabled-password --gecos '' app

USER app

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "main.py"]