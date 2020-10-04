# Lab 2
1. I have successfully installed python 3.8 isolated  environment using 
```bash
pip3 install pipenv 
pipenv --python 3.8
pipenv shell
```
2. Installed **requests** and **ntplib** libraries with their dependencies using `pipenv install requests ntplib`.
3. Created app.py script from given source. The result of execution is error message, if no URL provided, or UTC time, parsed from JSON. To expolore result of execution `python3 app.py` in virtual environment was used.
4. Installed **pytest** using `pipenv install pytest`.
5. Run unit tests with `pytest tests/tests.py`. All tests has passed.
6. Implemented `get_time_of_day_name()` function that returns name of day time or throws exception `RuntimeError` if argument does not contain time string.
7. Implemented `test_get_time_of_day()` unit test for check is function `get_time_of_day_name()` work correctly.
8. To redirect stdout stream to the file we should use `>` operator. To append stdout to the file `>>` needed. To store result of **app.py** execution to file `results.txt` command `python3 app.py > results.txt` should be used. To append result of unit tests execution `pytest tests/tests.py >> results.txt` should be executed. 
9. Wrote makefile for the repository. Add rules for set up the environment and install dependencies (`make install`), run unit tests (`make test`), run application (`make run`), and deploy (`make deploy`).
10. After running `make` (equal to `make all`) created a new pipenv environment, installed all project dep's, application, and unit test output stored to the `resrults.txt` file, committed and pushed to the remote.