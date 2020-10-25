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
1. Create container for minotoring utility:
   1. Create Dockerfile.monitor
   1. Build image with 
      ```
      $ sudo docker build --tag monitor_utility:v1.0.0 --file Dockerfile.monitor . 
      ```
   1. Run both containers.
      ```
      $ sudo docker run -it --name=django-page --rm --publish 8000:8000 sashakovalchuk/lab4:v1.0.1
      $ sudo docker run --net=host --name=monitor-util --rm -it monitor_utility:v1.0.0
      ```
      Monitoring container can access web app container.
      With `docker exec` I got access to container shell. Fragment of monitor logs:
      ```
      root@dhLaptop:/app# cat server.log 
      INFO 2020-10-04 23:52:09,752 root : Сервер доступний. Час на сервері: 2020-10-04T20:52:09.751245
      INFO 2020-10-04 23:52:09,752 root : Запитувана сторінка: : http://localhost:8000/health/
      INFO 2020-10-04 23:52:09,753 root : Відповідь сервера місти наступні поля:
      INFO 2020-10-04 23:52:09,753 root : Ключ: servername, Значення: lab server
      INFO 2020-10-04 23:52:09,753 root : Ключ: random, Значення: 184
      INFO 2020-10-04 23:52:09,753 root : Ключ: datetime, Значення: 2020-10-04T20:52:09.751245
      INFO 2020-10-04 23:52:09,753 root : Ключ: server_url, Значення: http://localhost:8000/health/
      INFO 2020-10-04 23:52:09,753 root : Ключ: server_iinfo, Значення: {'system': 'posix', 'user': 'dhdhxji', 'srv_pid': 227106}
      INFO 2020-10-04 23:52:09,753 root : Ключ: client_info, Значення: {'user agent': 'python-requests/2.24.0', 'remote addr': '127.0.0.1', 'remote host': ''}
      INFO 2020-10-25 17:30:56,407 root : Сервер доступний. Час на сервері: 2020-10-25T17:30:56.405639
      INFO 2020-10-25 17:30:56,407 root : Запитувана сторінка: : http://localhost:8000/health/
      INFO 2020-10-25 17:30:56,407 root : Відповідь сервера місти наступні поля:
      INFO 2020-10-25 17:30:56,407 root : Ключ: servername, Значення: lab server
      INFO 2020-10-25 17:30:56,407 root : Ключ: random, Значення: 85
      INFO 2020-10-25 17:30:56,407 root : Ключ: datetime, Значення: 2020-10-25T17:30:56.405639
      INFO 2020-10-25 17:30:56,407 root : Ключ: server_url, Значення: http://localhost:8000/health/
      INFO 2020-10-25 17:30:56,407 root : Ключ: server_iinfo, Значення: {'system': 'posix', 'srv_pid': 13}
      INFO 2020-10-25 17:30:56,407 root : Ключ: client_info, Значення: {'user agent': 'python-requests/2.24.0', 'remote addr': '172.17.0.1', 'remote host': ''}
      ```