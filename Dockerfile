FROM python:2.7-slim

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org

EXPOSE 80

ENV NAME world

CMD ["python", "main.py"]