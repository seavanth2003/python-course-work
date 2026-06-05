

conditional statements
-------------------------
1. simple if
2. if-else
3.if-else-else
4. Nested if


EX-IF
----------

s='python programming'
if 'python' in s:
    print('found')

if s[0]=='p':
    print('string startng with p')

EX-IF ELSE
------------

data=('koushal','98721')

username,password=input("Enter the username,password: ").split()
if data==(username,password):
    print("login successful")
else:
    print("un successful")

EX-IF-ELSE-ELSE
------------------

n= int(input("Enter the num: "))

if n>0:
    print("+ve")
elif n<0:
    print("-ve")
else:
    print("zero")


EX-NESTED IF
--------------

products={
    'laptop':9,
    'mouse':10,
    'keyboard':90,
    'phones':0
}

product=input("Enter the product: ")
if product in product:
    if products[product]!=0:
        print(f"you can buy{product}")
    else:
        print(f"{product} is out of stock")

else:
    print(f"{product} is not available")
    
