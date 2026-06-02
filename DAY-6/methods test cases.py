Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='python programming'
len(s)
18
min(s)
' '
max(s)
'y'
sorted(s)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
ord('a')
97
ord('A')
65
chr('p')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    chr('p')
TypeError: 'str' object cannot be interpreted as an integer
chr(8)
'\x08'


s='pYTHON programmING'
s.upper()
'PYTHON PROGRAMMING'
s.lower()
'python programming'
s.capitalize()
'Python programming'
s.title()
'Python Programming'
s.swapcase()
'Python PROGRAMMing'

s.center(38,'#')
'##########pYTHON programmING##########'
s.ljust(28,'&')
'pYTHON programmING&&&&&&&&&&'
s.rjust(76,'*')
'**********************************************************pYTHON programmING'
'1234'.zfill(4)
'1234'
'1234'.zfill(7)
'0001234'
'123'.zfill(100)
'0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000123'


s.find('p
       
SyntaxError: unterminated string literal (detected at line 1)
s.find('p')
       
0
s.rfind('m')
       
14
s.index('i')
       
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    s.index('i')
ValueError: substring not found
s.rindex('i')
       
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s.rindex('i')
ValueError: substring not found
s.count('o')
       
1
s..count('p','m')
       
SyntaxError: invalid syntax
s.count('p','m')
       
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s.count('p','m')
TypeError: slice indices must be integers or None or have an __index__ method
s.count('p')
       
2



s.replace('python','java')
       
'pYTHON programmING'
s
       
'pYTHON programmING'
s.replace('pyTHON','java')
       
'pYTHON programmING'
s.replace('pyTHON','java')
       
'pYTHON programmING'
s.replace('pYTHON ','java')
       
'javaprogrammING'

s.maketrans('pYTHON','123456')
       
{112: 49, 89: 50, 84: 51, 72: 52, 79: 53, 78: 54}
s.translate('pYTHON ','123456')
       
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    s.translate('pYTHON ','123456')
TypeError: str.translate() takes exactly one argument (2 given)
s.translate(s.maketrans('pYTHON ','123456'))
       
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    s.translate(s.maketrans('pYTHON ','123456'))
ValueError: the first two maketrans arguments must have equal length


s='java,python,c,c++'
       
s.split('-')
...        
['java,python,c,c++']
>>> s.split(',')
...        
['java', 'python', 'c', 'c++']
>>> s.split(',',2)
...        
['java', 'python', 'c,c++']
>>> s.rsplit(',',2)
...        
['java,python', 'c', 'c++']
>>> s.splitlines()
...        
['java,python,c,c++']
>>> '.join(s)
...        
SyntaxError: unterminated string literal (detected at line 1)
>>> ''.join(s)
...        
'java,python,c,c++'
>>> '-',.join(s)
...        
SyntaxError: invalid syntax
>>> '-'.join(s)
...        
'j-a-v-a-,-p-y-t-h-o-n-,-c-,-c-+-+'
>>> '#'.join(s)
...        
'j#a#v#a#,#p#y#t#h#o#n#,#c#,#c#+#+'
>>> 
>>> s.partition(',')
...        
('java', ',', 'python,c,c++')
>>> s.rpartition(',')
...        
('java,python,c', ',', 'c++')
>>> 
>>> 
>>> t="hello 😊"
...        
>>> t.encode()
...        
b'hello \xf0\x9f\x98\x8a'
>>> b'hello \xf0\x9f\x98\x8a'.decode()
...        
'hello 😊'
