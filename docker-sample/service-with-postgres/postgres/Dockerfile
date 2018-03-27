FROM registry.access.redhat.com/rhscl/postgresql-94-rhel7

ENV POSTGRESQL_USER ale7canna
ENV POSTGRESQL_PASSWORD 123123
ENV POSTGRESQL_DATABASE coindb
ENV POSTGRESQL_ADMIN_PASSWORD postgres

WORKDIR /usr/share/container-scripts/postgresql/start
COPY ./init-db/ /usr/share/container-scripts/postgresql/start/
