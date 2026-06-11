'''
seq: str,list,tuple,set,dict,range
for i in seq:
    #stmts
    '''

'''
pin=1234
for i in range(5):
    
    e_pin=int(input("Enter the pin: "))
    
    if e_pin==pin:
      print("Unlock the phone")
      break    
    else:
       print("Incorrect pin")
else:
    print("Try again after 60 sec")
'''

'''
l=[2,3,4,5,8,10,34,12]
search=int(input("Enter the element: "))
for i in range(len(l)):
    if l[i]==search:
        print(f'{search} is found at index-{i}')
        break
else:
    print(f'{search} is not found')
    '''

password=input("Enter your password: ")
if len(password)>=8:
    s=set()
    for i in password:
        if i.isupper():
            s.add('u')
        elif i.islower():
            s.add('l')
        elif i.isdigit():
                s.add('s')
        else:
                s.add('s')
        if len(s)==4:
            print("Strong password")
    else:
        print("Week password")
else:
    print("Week password")
    
            



