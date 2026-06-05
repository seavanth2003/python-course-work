Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d={}
d=dict()
type(d)
<class 'dict'>
d={'k1':'v1','k2':'v2'}
d
{'k1': 'v1', 'k2': 'v2'}
d[1]='int'
d
{'k1': 'v1', 'k2': 'v2', 1: 'int'}
d={}
d[1]='int'
d
{1: 'int'}
d[12.3]='float'
d
{1: 'int', 12.3: 'float'}
d['demo']='str'
d
{1: 'int', 12.3: 'float', 'demo': 'str'}
d[12+15j]='complex'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (12+15j): 'complex'}
d[(1,2,3,4}]='tuple'
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
d[(1,2,3,4)]='tuple'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (12+15j): 'complex', (1, 2, 3, 4): 'tuple'}
d['False']='bool'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (12+15j): 'complex', (1, 2, 3, 4): 'tuple', 'False': 'bool'}
d={}
d[1]=1
d
{1: 1}
d[23]=23.4
d[3]='fgfvf'
d[4]=34+9j
d[5]=[1,8,9]
d[6]=(8,4,1)
d[7]={9,4}
d[8]={2:2,3:3}
d[9]=False
d
{1: 1, 23: 23.4, 3: 'fgfvf', 4: (34+9j), 5: [1, 8, 9], 6: (8, 4, 1), 7: {9, 4}, 8: {2: 2, 3: 3}, 9: False}
d={}
d[1]=14
d
{1: 14}
d={}
d[1]=2
d[2]=2
d[3]=2
d[4]=2
d
{1: 2, 2: 2, 3: 2, 4: 2}
d[3]=
SyntaxError: invalid syntax
d[3]
2
d
{1: 2, 2: 2, 3: 2, 4: 2}
d={1:2,2:3,3:6,4:8,5:10,6:12}
d[4]
8
d[9]
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    d[9]
KeyError: 9
d[6]
12
d[2]
3
d[5]
10

d={'dinesh':45,'karthik':69,'ranjith':80,'pradeep':90}
d
{'dinesh': 45, 'karthik': 69, 'ranjith': 80, 'pradeep': 90}
d.get('karthik')
69
d.get('ranjt')
d
{'dinesh': 45, 'karthik': 69, 'ranjith': 80, 'pradeep': 90}
d.get('pradeep')
90
d.get('praveen','user not found')
'user not found'
d.get('dinesh','user not found')
45
d
{'dinesh': 45, 'karthik': 69, 'ranjith': 80, 'pradeep': 90}

'dinesh'in d
True
'ranjith' in d
True
'subbu' not in d
True
'praveen' in d
False
d.key()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    d.key()
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
d.keys()
dict_keys(['dinesh', 'karthik', 'ranjith', 'pradeep'])
d.values()
dict_values([45, 69, 80, 90])
d.items()
dict_items([('dinesh', 45), ('karthik', 69), ('ranjith', 80), ('pradeep', 90)])
sorted(d)
['dinesh', 'karthik', 'pradeep', 'ranjith']
max(d)
'ranjith'
min(d)
'dinesh'
len(d)
4
d
{'dinesh': 45, 'karthik': 69, 'ranjith': 80, 'pradeep': 90}


d['rishi']=86
d
{'dinesh': 45, 'karthik': 69, 'ranjith': 80, 'pradeep': 90, 'rishi': 86}
d.update({'praneeth':89,'sujith':50})
d
{'dinesh': 45, 'karthik': 69, 'ranjith': 80, 'pradeep': 90, 'rishi': 86, 'praneeth': 89, 'sujith': 50}
d.popitem()
('sujith', 50)
d
{'dinesh': 45, 'karthik': 69, 'ranjith': 80, 'pradeep': 90, 'rishi': 86, 'praneeth': 89}
d.popitem()
('praneeth', 89)
d
{'dinesh': 45, 'karthik': 69, 'ranjith': 80, 'pradeep': 90, 'rishi': 86}
d.pop('rishu
      
SyntaxError: unterminated string literal (detected at line 1)
d.oo
      
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    d.oo
AttributeError: 'dict' object has no attribute 'oo'
p
d.pop('rish
      
SyntaxError: unterminated string literal (detected at line 1)
d.pop('rishi')
      
86
del d['ranjith']
      
d
      
{'dinesh': 45, 'karthik': 69, 'pradeep': 90}
d.clear()
      
d
      
{}
d={'dinesh': 45, 'karthik': 69, 'ranjith': 80, 'pradeep': 90, 'rishi': 86, 'praneeth': 89, 'sujith': 50}
      
d.setdefault('sujith':50)
      
SyntaxError: invalid syntax
d.setdefault('sujith':0)
      
SyntaxError: invalid syntax
d.setdefault('sujith',0)
      
50
d
      
{'dinesh': 45, 'karthik': 69, 'ranjith': 80, 'pradeep': 90, 'rishi': 86, 'praneeth': 89, 'sujith': 50}
d.setdefault('pradeep',9)
      
90
d
...       
{'dinesh': 45, 'karthik': 69, 'ranjith': 80, 'pradeep': 90, 'rishi': 86, 'praneeth': 89, 'sujith': 50}
>>> 
>>> 
>>> 
>>> 
Warning (from warnings module):
  File "C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-8/coditional stmts.py", line 5
    3.if-else-else
SyntaxWarning: invalid decimal literal
>>> 
== RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-8/coditional stmts.py ==
found
string startng with p
>>> 
== RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-8/coditional stmts.py ==
found
string startng with p
Enter the username,password: 'koushal','98721'
Traceback (most recent call last):
  File "C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-8/coditional stmts.py", line 13, in <module>
    username,password=input("Enter the username,password: ").split()
ValueError: not enough values to unpack (expected 2, got 1)
>>> 
== RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-8/coditional stmts.py ==
found
string startng with p
Enter the username,password: koushal
Traceback (most recent call last):
  File "C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-8/coditional stmts.py", line 13, in <module>
    username,password=input("Enter the username,password: ").split()
ValueError: not enough values to unpack (expected 2, got 1)
>>> 
== RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-8/coditional stmts.py ==
found
string startng with p
Enter the username,password: koushal,98721
Traceback (most recent call last):
  File "C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-8/coditional stmts.py", line 13, in <module>
    username,password=input("Enter the username,password: ").split()
ValueError: not enough values to unpack (expected 2, got 1)
