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