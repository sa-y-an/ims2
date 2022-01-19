# Inventory Management System

Instuctions 

- If you use docker as a non-root user please run the commands as sudo

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
```
To run migrations use  (only run once at the start)
- Use 
```
docker exec -it django_container /bin/bash
```
It opens an interative shell where do - 
```
python3 manage.py migrate
```
