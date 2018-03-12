docker kill pg
docker run -d --name pg -p 5432:5432 -t postgres:alpine postgres
