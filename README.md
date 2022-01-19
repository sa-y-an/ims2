# IMS
- Inventory Management System
- Live Demo can be found at - https://shopify-ims.herokuapp.com/ (please allow sometime, while loading the first time, the heroku containers might wake up from a deep sleep after a long time).

### Installation Instructions

#### Pre-requisites
- Please install [docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/) for installation as this project uses multiple dependencies
- If you use docker as a non-root user please run the commands as sudo or [set up docker as a non root user](https://docs.docker.com/engine/install/linux-postinstall/)

- Once docker is installed create a ```.env``` in the ```core directory``` 
- Fill its content using .example.env file

Now run the following commands - 
```sh
docker-compose --env-file ./core/.env up
```
Once it runs and the terminal reads ```Quit the server with CONTROL-C.``` 

- your server starts running 

- Now create a new terminal and run the migrations only once at the start or anytime you change the models using- 
```sh
docker exec -it django_container /bin/bash
```
It opens an interative shell where you can migrate using - 
```sh
python3 manage.py migrate
```
- You app is now ready 
- Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see the magic

### Usage Guides 

- create a category 
- create a brand 
- create the attributes 
- create the product
- now create its inventory

### Features 

- Basic CRUD
- Product belongs categories and multiple variants of a product
- Image Thumbnail generation of an uploaded image automatically 