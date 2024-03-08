FROM python:3.10.13-bookworm

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN mkdir media

CMD python main.py