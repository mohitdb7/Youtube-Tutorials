# Docker commands

### Docker containers
To build and mount the custom images for backend and frontend
```
docker-compose up
```

To rebuild and start the container cleanly
```
docker-compose up --build
```

To run all instances, use docker compose container up command
```
docker-compose up
```

To stop all the container
Stop containers (but keep volumes/images):
```
docker-compose down
```

Stop containers remove volumes/images:
```
docker-compose down --rmi all --volumes
```

`--rmi all`: Remove all images used by any service.

`--volumes`: Remove named volumes declared in the volumes section of docker-compose.yml

To view all running containers
```
docker ps
```

To stop a running container
```
docker stop <container_name_or_id>
```
__________


### Docker images

When using the build in docker-compose then it will create the images by itself


To build image explicitly
```
docker build -t my-backend-image-name:latest -f path-to-dockerFile/Dockerfile .
```

In this case, use the image <image-name> in the `docker-compose.yml` file instead of build.

To view all the images
```
docker images
```

To get only image ids
```
docker images -q
```

To remove image (we can pass multiple image ids to delete multiple images)
```
docker rmi <image-id> <image-id>
```

Remove all docker images
```
docker rmi $(docker images -q)
```

_______


### Redis

Install Redis
```
brew redis
```

start redis
```
brew services start redis
```

Check if redis is running
```
redis-cli ping
```

stop redis
```
brew services stop redis
```