FROM python:3.6-slim
WORKDIR /app
COPY . /app
EXPOSE 5000
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "-u", "app_web.py"]