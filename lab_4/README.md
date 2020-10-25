# Lab 4
1. Learned about docker in the official documentation
1. Run following commands to test is docker installed successfully:
   ```
   sudo docker -v
   sudo docker -h
   sudo docker run docker/whalesay cowsay Docker is fun
    ```
   Output:
   ```
   $ sudo docker -v
   $ sudo docker -h
   $ sudo docker run docker/whalesay cowsay Docker is fun
   ``` 
   Execution output for these commands located at `test_output.txt` file of this repo.
1. Learned the Dockerfile documentation
1. Create new Dockerfile with Django web app from previous lab
1. Created new DockerHub [repository](https://hub.docker.com/repository/docker/sashakovalchuk/lab4) for this lab 
1. Build and push [image](https://hub.docker.com/layers/sashakovalchuk/lab4/v1.0.1/images/sha256-19555f3e782dcb33539f5948ba0b6432e318545da9f94a3286baac35496b5376?context=repo) to the repo:
   ```
   sudo docker build --tag sashakovalchuk/lab4:v1.0.0 .
   sudo docker push sashakovalchuk/lab4:v1.0.0
   ```
1. Run the docker image with 
   ```
   sudo docker run -it --name=django-page --rm --publish 8000:8000 sashakovalchuk/lab4:v1.0.0
   ```
   Web page works well