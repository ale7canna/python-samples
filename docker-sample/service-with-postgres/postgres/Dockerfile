FROM registry.access.redhat.com/rhscl/postgresql-94-rhel7

ENV POSTGRESQL_USER ale7canna
ENV POSTGRESQL_PASSWORD 123123
ENV POSTGRESQL_DATABASE coindb

WORKDIR /app
COPY creation_script.sql /app
#RUN psql -h localhost -p 5432 -U ale7canna -d coindb -f creation_script.sql
