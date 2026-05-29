Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
type(a)
<class 'int'>
t=99.01
type(t)
<class 'float'>
p=2+9j
type(p)
<class 'complex'>

s='python'
type(s)
<class 'str'>
s='python'
s='java'
s
'java'
s='python'
id(s)
1951721504416
s='java'
id(s)
1951729333856

1=[1,2,3,4]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
l=[1,2,3,4]
id(l)
1951721704384
l.append(600)
l.append(4000)
l
[1, 2, 3, 4, 600, 4000]
l=list()
type(l)
<class 'list'>

s=(1,2,3,4)
s
(1, 2, 3, 4)
type(s)
<class 'tuple'>
>>> g={1,3,5,7,9]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> g={1,3,5,7,9}
>>> type(g)
<class 'set'>
>>> s=set()
>>> id(s)
1951764902656
>>> e={"name":"pandu","age":22}
>>> e
{'name': 'pandu', 'age': 22}
>>> type(e)
<class 'dict'>
>>> id(e)
1951723983872
>>> 
>>> e.append("sex":"m")
SyntaxError: invalid syntax
>>> 
>>> 
>>> t=none()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    t=none()
NameError: name 'none' is not defined. Did you mean: 'None'?
>>> t=none
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    t=none
NameError: name 'none' is not defined. Did you mean: 'None'?
>>> t=None
>>> type(t)
<class 'NoneType'>
>>> 
>>> status=True
>>> status=False
>>> type(status)
<class 'bool'>
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
