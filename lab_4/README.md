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
1. Build and push [image](https://hub.docker.com/layers/sashakovalchuk/lab4/v1.0.0/images/sha256-93789be22975062e758180a33849582f9eab1b58f6f42711a86d82df7e20c4d5?context=repo) to the repo:
   ```
   sudo docker build --tag sashakovalchuk/lab4:v1.0.0 .
   sudo docker push sashakovalchuk/lab4:v1.0.0
   ```