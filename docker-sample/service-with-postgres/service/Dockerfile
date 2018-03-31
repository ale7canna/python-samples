FROM python:3.6-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "-u", "app_coin_service.py"]