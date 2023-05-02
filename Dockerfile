FROM python:3.8-slim

RUN apt-get update && apt-get install -y build-essential && apt-get install curl -y

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install debugpy

EXPOSE 5000

CMD ["python", "app.py"]