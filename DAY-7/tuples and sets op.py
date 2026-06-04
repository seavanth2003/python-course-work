Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s=(1,2,3,4,5)
s
(1, 2, 3, 4, 5)
t=()
t=(1,1,1,1)
t
(1, 1, 1, 1)
t=(1,1.1,'bgg',[])
t
(1, 1.1, 'bgg', [])
t=(10,20,30,40,50)
h=(90,70,60)
t
(10, 20, 30, 40, 50)
h
(90, 70, 60)
t+h
(10, 20, 30, 40, 50, 90, 70, 60)
t*4
(10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50)
t(1)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    t(1)
TypeError: 'tuple' object is not callable
t[0]
10
t[2]
30
t[4]
50
t
(10, 20, 30, 40, 50)
t[:3]
(10, 20, 30)
t[1:4]
(20, 30, 40)
10 in t
True
90 in t
False
50 not in t
False
40 in t
True
70 in h
True

sorted(t)
[10, 20, 30, 40, 50]
max(t)
50
min(t)
10
sum(t)
150
t.count(10)
1
t.index(10)
0


a=(1,2,3)
a
(1, 2, 3)
x,y,z=a

x
1
y
2
z
3
t=(1,2,3,[4,5,6],7,8)
t
(1, 2, 3, [4, 5, 6], 7, 8)
t[2]
3
t[4]
7
t[3]
[4, 5, 6]
t[2]
3
t[2]=4
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    t[2]=4
TypeError: 'tuple' object does not support item assignment
t[3]=6
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    t[3]=6
TypeError: 'tuple' object does not support item assignment
t[3].append(8)
t
(1, 2, 3, [4, 5, 6, 8], 7, 8)
t[3]
[4, 5, 6, 8]


s={1,2,3,4}
s
{1, 2, 3, 4}
s.add(1)
s
{1, 2, 3, 4}
s.add(56.676)
s
{1, 2, 3, 4, 56.676}
s.add("kjnk")
s
{1, 2, 3, 4, 'kjnk', 56.676}
s.add([1,2,3,4])
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    s.add([1,2,3,4])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
1 in s
True
2 in s
True
False in s
False


c={9,8,6,5,4,3,2}
l={8,6,5,4}
c|l
{2, 3, 4, 5, 6, 8, 9}
c.union(l)
{2, 3, 4, 5, 6, 8, 9}
c.intersection(l)
{8, 4, 5, 6}
c&l
{8, 4, 5, 6}
c-l
{9, 2, 3}
c^l
{2, 3, 9}
t
(1, 2, 3, [4, 5, 6, 8], 7, 8)

#{1} {2} {3} {5} {1,3} {3,6} {6,9} \

a<={1}
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    a<={1}
TypeError: '<=' not supported between instances of 'tuple' and 'set'
a >={1}
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    a >={1}
TypeError: '>=' not supported between instances of 'tuple' and 'set'
#{1}{2}{3}{5}{1,3}{1,2},{8,10}\

a >={1}
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    a >={1}
TypeError: '>=' not supported between instances of 'tuple' and 'set'
a <= {1,2,3,4,5,8,10,11,12}
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    a <= {1,2,3,4,5,8,10,11,12}
TypeError: '<=' not supported between instances of 'tuple' and 'set'
#{1}{2}{3}{5}{1,3}{1,2}{8,10}
a<={1}
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    a<={1}
TypeError: '<=' not supported between instances of 'tuple' and 'set'

++
SyntaxError: invalid syntax


++
SyntaxError: invalid syntax

a={1,2,3,4,5,6,7}
a
{1, 2, 3, 4, 5, 6, 7}
a.add(14)
a
{1, 2, 3, 4, 5, 6, 7, 14}
>>> a.update({19,12,36})
>>> a
{1, 2, 3, 4, 5, 6, 7, 36, 12, 14, 19}
>>> 
>>> a.pop()
1
>>> a.pop()
2
>>> a
{3, 4, 5, 6, 7, 36, 12, 14, 19}
>>> a.remove(4)
>>> a.discard(6)
>>> a
{3, 5, 7, 36, 12, 14, 19}
>>> a.discard(3)
>>> 
>>> a
{5, 7, 36, 12, 14, 19}
>>> 
>>> 
>>> b={1,2,4,56}
>>> a.intersection_update(b)
>>> a
set()
>>> b
{56, 1, 2, 4}
>>> c=b
>>> c.add(12)
>>> c
{1, 2, 4, 12, 56}
>>> a<={1,2,3,4,5,8,10,11,12}
True
>>> d=c.copy()
>>> d.add(14)
>>> c
{1, 2, 4, 12, 56}
>>> len(c)
5
>>> min(c)
1
>>> max(c)
56
>>> sorted(c)
[1, 2, 4, 12, 56]
>>> sum(c)
75
