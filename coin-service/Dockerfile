FROM alpine/git AS repo-env
WORKDIR /repo
RUN git clone https://github.com/ale7canna/python-samples

FROM python:3.6-slim AS build-env
WORKDIR /app
COPY --from=repo-env /repo/python-samples /app
RUN pip install -r requirements.txt
RUN mkdir result