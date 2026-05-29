Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
a
10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
bool(a)
True
b=10.6
int(b)
10
complex(b)
(10.6+0j)
set(b)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
list(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
str(b)
'10.6'
bool(b)
True
complex(b)
(10.6+0j)
a=2+9j
int(a)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(a)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'complex'
dict(a)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    dict(a)
TypeError: 'complex' object is not iterable
list(a)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list(a)
TypeError: 'complex' object is not iterable
str(a)
'(2+9j)'
bool(a)
True
tuple(a)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    tuple(a)
TypeError: 'complex' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    set(a)
TypeError: 'complex' object is not iterable
l='1','2','3','4','5'
int(l)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(l)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'tuple'
str(l)
"('1', '2', '3', '4', '5')"
float(l)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'tuple'
bool(l)
True
tuple(l)
('1', '2', '3', '4', '5')
set(l)
{'2', '4', '1', '3', '5'}
complex(l)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    complex(l)
TypeError: complex() argument must be a string or a number, not tuple
complex(l)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    complex(l)
TypeError: complex() argument must be a string or a number, not tuple
q=[1,2,3,4,5,6,7,8,9]
int(q)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    int(q)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(q)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    float(q)
TypeError: float() argument must be a string or a real number, not 'list'
complex(q)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    complex(q)
TypeError: complex() argument must be a string or a number, not list
str(q)
'[1, 2, 3, 4, 5, 6, 7, 8, 9]'
list(q)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
tuple(q)
(1, 2, 3, 4, 5, 6, 7, 8, 9)
set(q)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
dict(q)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    dict(q)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
bool(q)
True

t=(9,8,7,6,5,4,3,2,1)
int(t)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(t)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    complex(t)
TypeError: complex() argument must be a string or a number, not tuple
str(t)
'(9, 8, 7, 6, 5, 4, 3, 2, 1)'
list(t)
[9, 8, 7, 6, 5, 4, 3, 2, 1]
set(t)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
dict(t)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    dict(t)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
bool(t)
True

c={1,5,8,9,13,46}
int(c)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(c)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'set'
>>> complex(c)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    complex(c)
TypeError: complex() argument must be a string or a number, not set
>>> str(c)
'{1, 5, 8, 9, 13, 46}'
>>> list(c)
[1, 5, 8, 9, 13, 46]
>>> tuple(c)
(1, 5, 8, 9, 13, 46)
>>> dict(c)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    dict(c)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
>>> bool(c)
True
>>> 
>>> d=(1:2,3:6,4:8,5:10}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> d={1:2,3:6,4:8,5:10}
>>> int(d)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
>>> float(d)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'dict'
>>> str(d)+
SyntaxError: invalid syntax
>>> list(d)
[1, 3, 4, 5]
>>> str(d)
'{1: 2, 3: 6, 4: 8, 5: 10}'
>>> tuple(d)
(1, 3, 4, 5)
>>> set(d)
{1, 3, 4, 5}
>>> bool(d)
True
