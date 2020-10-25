import datetime
import sys
from random import randint


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform

def get_odd_even_numbers(is_even):
    offset = 1 if not is_even else 0
    return range(offset, 100, 2)

def possible_exception_func():
    if randint(0, 1) == 0:
        raise Exception('Possible function exception')