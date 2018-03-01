FROM python:3.6-slim AS build-env

WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt

#FROM gcr.io/distroless/python3
#WORKDIR /app
#COPY --from=build-env /app /app
#COPY --from=build-env /usr/local/lib/python3.5/site-packages/ /usr/local/lib/python3.5/site-packages/