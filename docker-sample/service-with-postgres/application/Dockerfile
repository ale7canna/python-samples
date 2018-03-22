FROM python:3.6-slim
WORKDIR /app
COPY . /app
EXPOSE 5000
RUN pip install --no-cache-dir -r application/requirements.txt
CMD ["python", "app_web.py"]