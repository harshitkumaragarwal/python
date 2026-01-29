Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 3+4
7
>>> #string initialization
>>> a = 'hello'
>>> b = 'world'
>>> 
>>> print(a + " " +b)
hello world
>>> print(a+3)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(a+3)
TypeError: can only concatenate str (not "int") to str
>>> print(a * 3)
hellohellohello
>>> python
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    python
NameError: name 'python' is not defined
>>> a='harshit'
>>> print(a*2)
harshitharshit
>>> print("on" in a)
False
>>> print("in" in a)
False
>>> print("p" in a)
False
>>> print("h" in a)
True
