# Docker commands

### Docker compose
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
```
Stop containers remove volumes/images:
docker-compose down -v

or

Stop containers (but keep volumes/images):
docker-compose down
```

To view all running containers
```
docker ps
```

To stop a running container
```
docker stop <container_name_or_id>
```
__________

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