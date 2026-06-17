#functions syntax
'''
def function_name(arg):

 function_name(para)

'''


'''
def wish(name):
    print(f"welcome to python course {name}!")

wish('kiran')
wish('ramu')
'''

'''
def iseven(num):
    if num%2==0:
        return f"{num}-Even number"
    else:
        return f"{num}-Odd number"
    
print(iseven(16))
print(iseven(19))
'''

'''
def  factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact
num=int(input("Enter the number: "))
print("Factorial : ",factorial(num))
'''

'''
def isprime(num):
    for i in range(2,num//2):
        if num%i==0:
            return f"{num}-Not prime number"
    return f"{num}-prime number"

num=int(input("Enter the number: "))
print(isprime(num))
'''

'''
def display(name,email,pwd):
    print("Name:", name)
    print("Email:", email)
    print("Password :", pwd)

display(name='sukumar',email='sukumar@gmail.com',pwd='sukumar@18')
display(email='ranjith@gmail.com',pwd='ranjith@16',name='ranjith')
display(pwd='pradeep@81',name='pradeep',email='pradeep@gmail.com')
'''

def display(*names):
    print("Names:", names)

display('subbu','dinesh','ranjith','praneeth')
display('sukumar','chanikya','nagendra','ranjith')
display('pradeep','subbu')


