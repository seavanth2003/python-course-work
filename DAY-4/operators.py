Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=20
b=60
a+b
80
a-b
-40
a*b
1200
a/b
0.3333333333333333
9/2
4.5
54/2
27.0
a**b
1152921504606846976000000000000000000000000000000000000000000000000000000000000
a%b
20
20%10.
0.0
100//25
4
a//b
0
45**5
184528125




a>b
False
a>=b
False
a<b
True
a<=b
True
a==b
False
a!=b
True


a=4
b=6
a=b
a+=b
a
12
b
6
a/=5
a
2.4
a*=b
a
14.399999999999999
b//=3
b
2
a%=2
a
0.3999999999999986
b%=8
b
2
a**=1
a
0.3999999999999986
b**=5
b
32
a**=b
a
1.8446744073707455e-13
b
32



a=20
b=10
a%10==0
True
a%20==0 and b%20==0 and a>b
False
a%20==0 or b%20==0 or a
True
a%20==0 or b%20==0 or a<b
True
a%20==0 or b%20==0 or a>b
True
a%25==0 or b%20==0 or a>b
True
a%27==0 or b%20==0 or a<b
False
not a>b
False
not a<b
True
not b>a
True
not b<a
False
a%20==0 and b%20==0 not a>b
SyntaxError: invalid syntax
a%20==0 and b%20==0 or not a>b
False



#str,tuple,list,set,dict
a='python programming '
a
'python programming '
r in a
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    r in a
NameError: name 'r' is not defined
'ar' in a
False
'r' in a
True
'python' in a
True
'of' not in a
True
'programming' not in a
False
l=['king','pradeep','chanikya']
l
['king', 'pradeep', 'chanikya']
'pradeep' in l
True
'predep' in l
False
'king' not in l
False
'ashok' not in l
True
k=("myself', 'codegnan',institute','pause')
   
SyntaxError: unterminated string literal (detected at line 1)
k=('myself', 'codegnan','institute','pause')
   
k
   
('myself', 'codegnan', 'institute', 'pause')
'myself' in k
   
True
'myself' not in k
   
False
'codegnan' not in k
   
False
s={1,2,3,4,}
   
s
   
{1, 2, 3, 4}
1 in s
   
True
6 not in s
   
True
1234 in s
   
False
1,3,4 in s
   
(1, 3, True)
d={"egg":10, "oil"=150,"sugar"=29}
   
SyntaxError: ':' expected after dictionary key
d={"egg":10, "oil":150,"sugar":29}
   
d
   
{'egg': 10, 'oil': 150, 'sugar': 29}
'sugar' in d
   
True
"egg" in d
   
True
"egg" not in d
   
False
"sugar":29 in d
   
SyntaxError: illegal target for annotation
29 in d
   
False



m=[1,2,3,4,5]
   
k=[1,2,3,4,5]
   
m==k
   
True
k==m
   
True
n=m
   
n
   
[1, 2, 3, 4, 5]
n==m
   
True
n is m
   
True
n is k
   
False
id(n)
   
2409640608704
id(k)
   
2409641776640
n is not k
   
True
n is not m
   
False
k is m
   
False
k is not n
   
True



>>> 
>>> 8 & 14
...    
8
>>> 8 & 7
...    
0
>>> 8|9
...    
9
>>> 8 | 7
...    
15
>>> 10^11
...    
1
>>> 19^2
...    
17
>>> 100^2
...    
102
>>> 20^2
...    
22
>>> 19|5
...    
23
>>> ~12
...    
-13
>>> ~17
...    
-18
>>> 1000^100000
...    
99656
>>> 3>>2
...    
0
>>> 4>>5
...    
0
>>> 7<<2
...    
28
>>> 15>>3
   
1
16<<1
   
32
4<<2
   
16




a=2
   
b=12.34
   
c='python'
   
print(a,b,c)
   
2 12.34 python
print('a'=,a,'b'=,b'c'=,c)
   
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
print('a=',a,'b=',b'c=',c)
   
a= 2 b= b'c=' python
print('a=',a,'b=',b'c=',c,sep='')
   
a=2b=b'c='python
print('a=',a,'b=',b'c=',c,sep='\t')
   
a=	2	b=	b'c='	python
print('a=',a,'b=',b'c=',c,sep='\n')
   
a=
2
b=
b'c='
python
print("a=",a,'b=',b,'c=',c,sep='',end='@@@@)
      
SyntaxError: unterminated string literal (detected at line 1)
print("a=",a,'b=',b,'c=',c,sep='',end='@@@@')
      
a=2b=12.34c=python@@@@
print(f'a={a] b={b} c={c}')
      
SyntaxError: f-string: unmatched ']'
print(f'a={a} b={b} c={c}')
      
a=2 b=12.34 c=python
print('a=%d b=%.2f c=%s'%(a,b,c))
      
a=2 b=12.34 c=python
print('a={} b={} c={}'. format(a,b,c))
      
a=2 b=12.34 c=python
print('a={2} b={1} c={0}'. format(a,b,c))
      
a=python b=12.34 c=2
