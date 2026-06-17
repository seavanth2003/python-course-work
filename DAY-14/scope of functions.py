'''
def display():  (local access)
    n=10
    print("Inside: ",n)
    

display()
print("outside: ",n)
'''

'''
n=1000                     (Global access)
def display():
     print("Inside: ",n)
display()
print("outside: ",n)
'''
'''
def display():
    global n
    n =19
    print("inside: ",n)
    
display()
print("outside:",n)
'''

'''
def display(n):         
    #global n
    n +=19
    print("inside: ",n)
n=10   
display(n)
print("outside:",n)
'''

'''
def display():        (Global keyword)
    global n
    n +=29
    print("inside: ",n)
n=11
display()
print("outside: ",n)
'''

'''
def outer():               (nonlocal keyword)
    n=10
    def inner():
        nonlocal n
        n+=19
        print("Inner function:",n)
    inner()
    print("outer function:",n)
outer()
'''


        
