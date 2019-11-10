# IndexError is thrown when trying to access an item at an invalid index.
>>> L1=[1,2,3]
>>> L1[3]
'''
Traceback (most recent call last):
File "<pyshell#18>", line 1, in <module>
L1[3]
IndexError: list index out of range
'''

#KeyError is thrown when a key is not found.
>>> D1={'1':"aa", '2':"bb", '3':"cc"}
>>> D1['4']
'''
Traceback (most recent call last):
File "<pyshell#15>", line 1, in <module>
D1['4']
KeyError: '4'
'''

# ModuleNotFoundError is thrown when a module could not be found.
>>> import notamodule
'''
Traceback (most recent call last):
File "<pyshell#10>", line 1, in <module>
import notamodule
ModuleNotFoundError: No module named 'notamodule'
'''

# ImportError is thrown when a specified function can not be found.
>>> from math import cube
'''
Traceback (most recent call last):
File "<pyshell#16>", line 1, in <module>
from math import cube
ImportError: cannot import name 'cube' 
'''

# ValueError is thrown when a function's argument is of an inappropriate type.
>>> int('xyz')
'''
Traceback (most recent call last):
File "<pyshell#14>", line 1, in <module>
int('xyz')
ValueError: invalid literal for int() with base 10: 'xyz'
'''


# NameError is thrown when an object could not be found.
>>> age
'''
Traceback (most recent call last):
File "<pyshell#6>", line 1, in <module>
age
NameError: name 'age' is not defined
'''


#ZeroDivisionError is thrown when the second operator in the division is zero.
>>> x=100/0
'''
Traceback (most recent call last):
File "<pyshell#8>", line 1, in <module>
x=100/0
ZeroDivisionError: division by zero 
'''
