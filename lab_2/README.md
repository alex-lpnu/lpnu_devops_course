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