# Lab 2a
1. Installed python 3.8, pip package manager
   ```bash
   sudo apt install python3 python3-pip
   ```
   Also look over the official python documentation, pep8 style guide
1. Created `script.py` python script, set execution permissions with `sudo chmod u+x script.py`:
   1. Printing built-in constants and literals:
        ```python
            print('First built-in constant', False)
            print('Second built-in constant', True)
            print('Third built-in constant', None)
            print('4th built-in constant', NotImplemented)
        ```
        Script execution output:
        ```
            $ ./script.py 
            First built-in constant False
            Second built-in constant True
            Third built-in constant None
            4th built-in constant NotImplemented
        ```
   1. Printing built-in function example:
        ```python
            print('Eval call example', eval('abs(-12.5)'))
            print('Map call example', tuple(map(len, ('string1', 'wow', 'another string'))))
        ```
        Execution result:
        ```
            Eval call example 12.5
            Map call example (7, 3, 14)
        ```
   1. Implemented loops and if condition example:
        ```python
            from random import randint

            print('For loop and if condition example')
            if randint(0, 1):
                for num in range(1, 10, 2):
                    print(num)
            else:
                for num in range(0, 10, 2):
                    print(num)
        ```
        Execution output:
        ```
            For loop and if condition example
            0
            2
            4
            6
            8
        ``` 
   1. Implemented try/except/finally example:
        ```python
            try:
                open('non-existiong-filepath', 'r')
            except FileNotFoundError as e:
                print('Error occurrend while opening the file: ', e)
            finally:
                print('Finally stuff')
        ``` 
        Execution result:
        ```
            Error occurrend while opening the file:  [Errno 2] No such file or directory: 'non-existiong-filepath'
            Finally stuff
        ```
   1. Implemented context manager example:
        ```python
            class ContextManagerExample:
                def __init__(self):
                    print(self.__class__.__name__, 'init')

                def __enter__(self):
                    print(self.__class__.__name__, 'enter')

                def __exit__(self, exc_type, exc_val, exc_cb):
                    print(self.__class__.__name__, 'exit')

            with ContextManagerExample() as obj:
                print("Context object stuff")
        ```
        Execution output: 
        ```
            ContextManagerExample init
            ContextManagerExample enter
            Context object stuff
            ContextManagerExample exit
        ```
   1. Lambda function example:
        ```python
            print('Factorial 4th power example: ', '10^4 = ', (lambda n: n*n*n*n)(10))
        ```
        Execution output:
        ```
            Factorial 4th power example:  10^4 =  10000
        ```
            Lambda function (aka anonymous function) is a function which does not have a unique identifier for access
1. Create directory structure
   1. Execute python in this directory. Output:
        ```
            We are in the __main__
            2020-10-25 14:59:22.890612
            linux
        ```
   1. This application parse command line arguments and print it, system information such as current system time and platform name. This information retrieved from `common` module (located in modules directory).
      1. When run the program with `-h` option, help will be displayed.
        ```
            $ python3 . -h
            usage: . [-h] [-o OPT] [-l]

            Приклад передачі аргументів у Python програму.

            optional arguments:
            -h, --help            show this help message and exit
            -o OPT, --optional OPT
                                    Цей параметр є вибірковим.
            -l, --logs            Якщо виконати команду з цим параметром будуть виводитись логи.
        ``` 
      1. It run application with `-o This text shold be displayed"` argument string will be displayed too:
        ```
            $ python3 . -o "This text shold be displayed"
            We are in the __main__
            2020-10-25 15:50:41.769153
            linux
            З консолі було передано аргумент
            ========== >> This text shold be displayed << ==========
        ```
      1. When run application with `-l` option, output will be like:
        ```
            $ python3 . -l
            2020-10-25 15:54:20,216 root INFO: Тут буде просто інформативне повідомлення
            2020-10-25 15:54:20,216 root WARNING: Це Warning повідомлення
            2020-10-25 15:54:20,216 root ERROR: Це повідомлення про помилку
        ```
   1. Implemented function `get_odd_even_numbers(is_even)` in common module. 
        ```python
            def get_odd_even_numbers(is_even):
            offset = 1 if not is_even else 0
            return range(offset, 100, 2)
        ```
        Output:
        ```
            $ python3 .
            We are in the __main__
            2020-10-25 16:06:38.533879
            linux
            Numbers
            0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98
        ```
   1. Implemented function with possible exception:
        ```python
            def possible_exception_func():
                if randint(0, 1) == 0:
                    raise Exception('Possible function exception')
        ```
        Output:
        ```
            $ python3 .
            We are in the __main__
            2020-10-25 16:11:33.367374
            linux
            Numbers
            0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 
            2020-10-25 16:11:33,367 root ERROR: Function raised exceptionPossible function exception

            $ python3 .
            We are in the __main__
            2020-10-25 16:11:34.004534
            linux
            Numbers
            0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 
            2020-10-25 16:11:34,004 root INFO: Function does not raised exception
        ```