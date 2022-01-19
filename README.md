# Inventory Management System

Instuctions 
- Run Docker
```sh
docker build --tag python-django .
docker run --publish 8000:8000 python-django
```
- Run docker-compose 
```sh
docker-compose up
```

With Postgress
```
docker-compose build
docker-compose up
docker exec -it django_container /bin/bash
```