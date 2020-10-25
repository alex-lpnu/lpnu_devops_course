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