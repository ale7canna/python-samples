FROM python:3.6-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r service/requirements.txt
CMD ["python", "app_coin_service.py"]