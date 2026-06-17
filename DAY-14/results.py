Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

================================================= RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/scope of functions.py ================================================
Inside:  10
Traceback (most recent call last):
  File "C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/scope of functions.py", line 5, in <module>
    print("outside: ",n)
NameError: name 'n' is not defined

= RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/scope of functions.py
Inside:  10
outside:  10

= RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/scope of functions.py
Inside:  1000
outside:  1000

= RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/scope of functions.py
inside:  19
outside: 19

= RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/scope of functions.py
Traceback (most recent call last):
  File "C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/scope of functions.py", line 24, in <module>
    display()
  File "C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/scope of functions.py", line 21, in display
    n+=19
UnboundLocalError: cannot access local variable 'n' where it is not associated with a value

= RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/scope of functions.py
inside:  29
outside: 10

= RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/scope of functions.py
inside:  19
outside: 19

= RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/scope of functions.py
inside:  29
outside: 10

= RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/scope of functions.py
inside:  40
outside:  40

= RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/scope of functions.py
Inner function: 29
outer function: 29

=== RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/pass by value.py ==
Inside: False
Outside: True

=== RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/pass by value.py ===
Inside: {1: 1, 2: 2, 3: 3, 4: 4}
Outside: {1: 1, 2: 2, 3: 3, 4: 4}

=== RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/pass by value.py ===
Inside: (1, 2, 3)
Outside: (4, 5, 6)

=== RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/pass by value.py ===
Inside: (3+1j)
Outside: (4+5j)

=== RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/pass by value.py ===
Inside: {6}
Outside: {1, 2, 3, 4, 5}

=== RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/pass by value.py ===
Inside: {1, 2, 3, 4, 5, 6}
Outside: {1, 2, 3, 4, 5, 6}

=== RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/pass by value.py ===
Traceback (most recent call last):
  File "C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/pass by value.py", line 12, in <module>
    update(n)
  File "C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/pass by value.py", line 8, in update
    n.append(8)
AttributeError: 'tuple' object has no attribute 'append'

=== RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/pass by value.py ===
Traceback (most recent call last):
  File "C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/pass by value.py", line 12, in <module>
    update(n)
  File "C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/pass by value.py", line 8, in update
    n.add(8)
AttributeError: 'tuple' object has no attribute 'add'

=== RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/pass by value.py ===
Inside: 8
Outside: (1, 2, 3, 4, 5, 6, 7)

=== RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/pass by value.py ===
Inside: (1, 2, 3, 4, 5, 6, 7)
Outside: (1, 2, 3, 4, 5, 6, 7)

==== RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/recurssions.py ====

==== RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/recurssions.py ====
5 4 3 2 1 

==== RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/recurssions.py ====
1 2 3 4 5 

==== RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/recurssions.py ====
1 2 3 4 5 

==== RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/recurssions.py ====
0

==== RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/recurssions.py ====
210

==== RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/recurssions.py ====
15

==== RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/recurssions.py ====
0

==== RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/recurssions.py ====
Traceback (most recent call last):
  File "C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/recurssions.py", line 33, in <module>
    print(sumofdigits(5))
  File "C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/recurssions.py", line 32, in sumofdigits
    return n*sumofdigits(n-1)
  File "C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/recurssions.py", line 32, in sumofdigits
    return n*sumofdigits(n-1)
  File "C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/recurssions.py", line 32, in sumofdigits
    return n*sumofdigits(n-1)
  [Previous line repeated 2 more times]
TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
>>> 
==== RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/recurssions.py ====
120
>>> 
==== RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/recurssions.py ====
Traceback (most recent call last):
  File "C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/recurssions.py", line 41, in <module>
    print(power(2,5))
  File "C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/recurssions.py", line 40, in power
    return base*power(base,pow-1)
NameError: name 'base' is not defined. Did you mean: 'bas'?
>>> 
==== RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/recurssions.py ====
32
6561
>>> 
==== RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/recurssions.py ====
Traceback (most recent call last):
  File "C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/recurssions.py", line 52, in <module>
    print(reveseofstr("python"))
NameError: name 'reveseofstr' is not defined. Did you mean: 'reverseofstr'?
>>> 
==== RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/recurssions.py ====
nohtyp
>>> 
==== RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-14/recurssions.py ====
gnimmargorp nohtyp
