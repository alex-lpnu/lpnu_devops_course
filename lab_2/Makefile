RESULT_FILE_PATH="results.txt"
TEST_FILE_PATH=$(RESULT_FILE_PATH)

all: install test run deploy

install:
	@echo "Setting up pipenv environment..."
	pipenv --python 3.8 
	pipenv install requests
	pipenv install ntplib
	pipenv install pytest

test:
	@echo "Running tests..."
	@echo "==== [$$(date)] ====" >> $(TEST_FILE_PATH)
	pipenv run pytest tests/tests.py >> $(TEST_FILE_PATH)

test-cli:
	pipenv run pytest tests/tests.py

run:
	@echo "Running app..."
	@echo "==== [$$(date)] ====" >> $(RESULT_FILE_PATH)
	pipenv run python3 app.py >> $(RESULT_FILE_PATH)

deploy:
	@echo "Deploying"
	git add $(RESULT_FILE_PATH)
	git add $(TEST_FILE_PATH)
	git commit -m "Lab 2: [deploy] $$(date)"
	git push origin lab2