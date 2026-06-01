Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name=input("enter your name: ")
enter your name: pandu
name
'pandu'
name=int(input("enter your age: "))
enter your age: 29
name
29
age=int(input("enter your age: "))
enter your age: 26
age
26
type(age)
<class 'int'>
gpa=float(input('enter the gpa: "))
                
SyntaxError: unterminated string literal (detected at line 1)
gpa=float(input("enter the gpa: "))
                
enter the gpa: 8.7
gpa
                
8.7
type(gpa)
                
<class 'float'>

'pandu kiran ranjith ajay'
                
'pandu kiran ranjith ajay'
'pandu kiran ranjith ajay'.split('')
                
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    'pandu kiran ranjith ajay'.split('')
ValueError: empty separator
'pandu kiran ranjith ajay'.split(' ')
                
['pandu', 'kiran', 'ranjith', 'ajay']
name=input("enter your names: ").split()
                
enter your names: kiran suji reddy veda
name
                
['kiran', 'suji', 'reddy', 'veda']
name=tuple(input("enter you topics: ").split())
                
enter you topics: paper book phone python
name
                
('paper', 'book', 'phone', 'python')
op=set(input("enter the operators: ").split())
                
enter the operators: in out not in in is and or and or
op
                
{'or', 'not', 'is', 'and', 'in', 'out'}
type(op)
                
<class 'set'>
type(name)
                
<class 'tuple'>
type(name)
                
<class 'tuple'>
int=int(input("enter your num: ").split())
                
enter your num: 1 4 6 7 18 20
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    int=int(input("enter your num: ").split())
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
list(map(int(input("enter your marks: ").split())))
                
enter your marks: 1 3 5 6 89
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    list(map(int(input("enter your marks: ").split())))
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
list(map(int,input("enter your marks: ").split()))
                
enter your marks: 1 3 56 79 245
[1, 3, 56, 79, 245]
prices=tuple(map(int,input("enter your prices: ").split()))
                
enter your prices: 4789 1234 0986 9567
prices
                
(4789, 1234, 986, 9567)
rat=set(map(int,input("enter your rating: ").split()))
                
enter your rating: 5 4 3 2 1 4 5 3 2 1
rat
                
{1, 2, 3, 4, 5}
per=list(map(float,input("enter the per's: ").split()))
                
enter the per's: 12.6 98.9 76.8 89.0
per
                
[12.6, 98.9, 76.8, 89.0]
mark=tuple(map(float,input("enter your marks: ").split()))
                
enter your marks: 23445 5667 7894 7779
mmark
                
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    mmark
NameError: name 'mmark' is not defined. Did you mean: 'mark'?
mark
                
(23445.0, 5667.0, 7894.0, 7779.0)
prices=set(map(float,input("enter the prices: ").split()))
                
enter the prices: 2999 7678 68990 8 17
prices
                
{7678.0, 8.0, 17.0, 2999.0, 68990.0}
a,b=10,20
                
a
                
10
b
                
20
username,password=input("enter the username & password: ").split()
                
enter the username & password: pandu@gmail.com 1234
username
                
'pandu@gmail.com'
password
                
'1234'
a,b,c,d=list(map(int,input("enter the 4 sides: ").split()))
                
enter the 4 sides: 4 4 5 6
a
                
4
b
                
4
c
                
5
d
                
6
price,discount=list(map(float,input("enter the prices, discount: ").split()))
                
enter the prices, discount: 56000 20.0
price
                
56000.0
discount
                
20.0


a=eval(input())
                
3456
a
                
3456
a=eval(input())
                
1,2,3,4
a
                
(1, 2, 3, 4)
a=eval(input())
                
"python"
a
                
'python'
type(a)
                
<class 'str'>
a=eval(input())
                
True
a
                
True
type(a)
                
<class 'bool'>
c=eval(input())
                
{"python":20}
c
                
{'python': 20}
type(c)
                
<class 'dict'>
c=eval(input())
                
{"python","king","queen"}
c
                
{'king', 'queen', 'python'}
type(c)
                
<class 'set'>


a='kumar'
                
b='swamy'
                
a+b
                
'kumarswamy'
a*20
                
'kumarkumarkumarkumarkumarkumarkumarkumarkumarkumarkumarkumarkumarkumarkumarkumarkumarkumarkumarkumar'
b*999
                

b*8
                
'swamyswamyswamyswamyswamyswamyswamyswamy'
'ranjith'*8
                
'ranjithranjithranjithranjithranjithranjithranjithranjith'




names=' python veda vamsi ranjith pradeep'
                
names[4]
                
'h'
names[5]
                
'o'
>>> names[8]
...                 
'v'
>>> names[:6]
...                 
' pytho'
>>> names[:7]
...                 
' python'
>>> names[8:12]
...                 
'veda'
>>> names[14:18:2]
...                 
'as'
>>> names[13:]
...                 
'vamsi ranjith pradeep'
>>> names[13:18:2]
...                 
'vmi'
>>> names[-6:]
...                 
'radeep'
>>> names[-1:-7]
...                 
''
>>> names[-7:-1]
...                 
'pradee'
>>> names.upper()
...                 
' PYTHON VEDA VAMSI RANJITH PRADEEP'
>>> names.lower()
...                 
' python veda vamsi ranjith pradeep'
>>> min(names)
...                 
' '
>>> max(names)
...                 
'y'
>>> sorted(names)
...                 
[' ', ' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'd', 'd', 'e', 'e', 'e', 'h', 'h', 'i', 'i', 'j', 'm', 'n', 'n', 'o', 'p', 'p', 'p', 'r', 'r', 's', 't', 't', 'v', 'v', 'y']
