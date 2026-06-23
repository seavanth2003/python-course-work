Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

= RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-17/list comprehensions.py
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]

= RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-17/list comprehensions.py
['o', 'o', 'a', 'i']
['o', 'o', 'a', 'i']

= RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-17/list comprehensions.py
[0, 2, 4, 0, 6, 0, 8, 10, 20, 46, 80]
[0, 2, 4, 0, 6, 0, 8, 10, 20, 46, 80]

= RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-17/list comprehensions.py
Enter the number-1: 10
Enter the number-2: 3
Enter the number-3: 6
Enter the number-4: 199
Enter the number-5: 7
Enter the number-6: 48
Enter the number-7: 2899
Enter the number-8: 90
Enter the number-9: 28
Enter the number-10: 10
[10, 3, 6, 199, 7, 48, 2899, 90, 28, 10]

= RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-17/list comprehensions.py
[1, 2, 3, 1, 2, 3, 1, 2, 3]
Traceback (most recent call last):
  File "C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-17/list comprehensions.py", line 70, in <module>
    l1=[j for i in rnage(3) for j in range(1,4)]
NameError: name 'rnage' is not defined. Did you mean: 'range'?

= RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-17/list comprehensions.py
[1, 2, 3, 1, 2, 3, 1, 2, 3]
[1, 2, 3, 1, 2, 3, 1, 2, 3]

= RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-17/list comprehensions.py
[[1, 2, 3], [1, 2, 3], [1, 2, 3]]

= RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-17/list comprehensions.py
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10} {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

= RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-17/list comprehensions.py
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

= RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-17/list comprehensions.py
Enter your marks-1: 80
Enter your marks-2: 70
Enter your marks-3: 90
Enter your marks-4: 100
Enter your marks-5: 99
{99, 100, 70, 80, 90}

= RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-17/list comprehensions.py
Enter your name-1: sujith
Enter your name-2: ramu
Enter your name-3: pradeep
Enter your name-4: ranjith
Enter your name-5: sai
Traceback (most recent call last):
  File "C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-17/list comprehensions.py", line 91, in <module>
    l1={int(input(f" Mr {name} Enter your marks-{i+1}: "))for i in range(5)}
NameError: name 'name' is not defined

= RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-17/list comprehensions.py
Traceback (most recent call last):
  File "C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-17/list comprehensions.py", line 90, in <module>
    l={input(f"Enter your name-{i+1}: ",{name})for i in range(5)}
NameError: name 'name' is not defined

= RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-17/list comprehensions.py
Enter your name-1: ramu
Enter your name-2: ranjith
Enter your name-3: kumar
Enter your name-4: pradeep
Enter your name-5: sai
 Mr {'kumar', 'pradeep', 'ramu', 'sai', 'ranjith'} Enter your marks-1: 
= RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-17/list comprehensions.py
Enter your name: ramu
Enter your marks: ranjith
Traceback (most recent call last):
  File "C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-17/list comprehensions.py", line 90, in <module>
    res={input("Enter your name: "):int(input("Enter your marks: "))
ValueError: invalid literal for int() with base 10: 'ranjith'

= RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-17/list comprehensions.py
Enter your name: ramu
Enter your marks: kumar
Traceback (most recent call last):
  File "C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-17/list comprehensions.py", line 90, in <module>
    res={input("Enter your name: "):int(input("Enter your marks: "))
ValueError: invalid literal for int() with base 10: 'kumar'
>>> 
= RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-17/list comprehensions.py
Enter the name: eshwar
Enter the mark: ramu
Traceback (most recent call last):
  File "C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-17/list comprehensions.py", line 90, in <module>
    res={input("Enter the name: "):int(input("Enter the mark: "))
ValueError: invalid literal for int() with base 10: 'ramu'
>>> 
= RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-17/list comprehensions.py
Enter the name: ramu
Enter the mark: ranjith
Traceback (most recent call last):
  File "C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-17/list comprehensions.py", line 90, in <module>
    res={input("Enter the name: "):int(input("Enter the mark: "))for i in range(5)}
ValueError: invalid literal for int() with base 10: 'ranjith'
>>> 
= RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-17/list comprehensions.py
Enter the name: ramu
Enter the mark: pradeep
Traceback (most recent call last):
  File "C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-17/list comprehensions.py", line 90, in <module>
    res={input("Enter the name: "): int(input("Enter the mark: "))for i in range(5)}
ValueError: invalid literal for int() with base 10: 'pradeep'
>>> 
= RESTART: C:/Users/HP/OneDrive/Desktop/python-course-work/DAY-17/list comprehensions.py
Enter the name: ramu
Enter the mark: 90
Enter the name: kishore 
Enter the mark: 100
Enter the name: ranjith 99
Enter the mark: 99
Enter the name: pradeep
Enter the mark: 100
Enter the name: sai
Enter the mark: 100
{'ramu': 90, 'kishore ': 100, 'ranjith 99': 99, 'pradeep': 100, 'sai': 100}
