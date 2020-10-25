# Lab 5
1. I have read about docker-compose in official doc
1. I have read about flask at official web-page
1. Learn about YAML format
1. Create empty project in this directory
1. Create `my_app` dir for project, `tests` dir for unit tests. In project requirements we can see `flask` and `redis` packages. In unit test deps there are `pytest` and `requests`
1. Install deps, run flask app, check is project in working state, run tests
   ```
   pipenv --python 3.8
   pipenv install -r requirements.txt
   pipenv run python app.py
   ```
   Run tests:
   ```
   pipenv run pytest test_app.py --url http://localhost:5000
   ```
   There is some troubles with unit tests. It fails a few times because before start the server a few thing should be resolved:
   1. On local machine (or anywhere in the network) must be running Redis server. Also app should be configured to use it.
   2. App could not automitically create logs directory. I created it manually. 

   After these manipulations tests passes and all the web pages works fine.
1. Add Dockerfiles's for app and unit tests, create Makefile for deploying.
1. Makefile consists of the next rules:
   - app - run `docker build` for an `Dockerfile.app`, build application container
   - tests - run `docker build` for an `Dockerfile.tests`, build test app container
   - run - create a docker container network, run the redis container, run the app container 
   - test-app - run test app container
   - docker-prune - docker prune (removes all unused containers, networks, volumes, images)