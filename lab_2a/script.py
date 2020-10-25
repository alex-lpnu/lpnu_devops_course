#!/usr/bin/python3

print('First built-in constant', False)
print('Second built-in constant', True)
print('Third built-in constant', None)
print('4th built-in constant', NotImplemented)

#Std functions example
print('Eval call example', eval('abs(-12.5)'))
print('Map call example', tuple(map(len, ('string1', 'wow', 'another string'))))

#Loops and conditions example
from random import randint

print('For loop and if condition example')
if randint(0, 1):
    for num in range(1, 10, 2):
        print(num)
else:
    for num in range(0, 10, 2):
        print(num)
 
#Exceptions
try:
    open('non-existiong-filepath', 'r')
except FileNotFoundError as e:
    print('Error occurrend while opening the file: ', e)
finally:
    print('Finally stuff')