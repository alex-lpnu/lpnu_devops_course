#!/usr/bin/python3

print('First built-in constant', False)
print('Second built-in constant', True)
print('Third built-in constant', None)
print('4th built-in constant', NotImplemented)

#Std functions example
print('Eval call example', eval('abs(-12.5)'))
print('Map call example', tuple(map(len, ('string1', 'wow', 'another string'))))