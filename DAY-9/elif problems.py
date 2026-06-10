'''
data={
    'subbu':{'status':True,'python': 90, 'mysql':93, 'flask':95},
    'ranjith':{'status':True,'python': 34, 'mysql':13, 'flask':45},
    'kumar':{'status':False,'python': None, 'mysql':None, 'flask':None},
    'crs':{'status':True,'python': 50, 'mysql':43, 'flask':65},
    'ajay':{'status':True,'python': 49, 'mysql':33, 'flask':20},
    }
name=input("Enter the name: ")

if name in data:
    if data[name]['status']:
        total=data[name]['python']+data[name]['mysql']+data[name]['flask']
        avg=total/3
        if avg>30:
            print(f"congrations {name}, you got first class!!!")
        elif avg>70:
                print(f"Good {name}, keep it up next time")
        elif avg>35:
            print(f"Better {name}, work hard next time!")
        else:
            print(f"{name},you have failed in the exam Bring you parents")
    else:
        print(f"{name} didn't write the exam")
else:
    print(f"{name}'s data not found")
'''

'''
budget=int(input("Enter the budget: "))
if budget >50000:
    print("you can go for the trip")
e
elif budget >30000:
    print("you can go for pub")
elif budget>10000:
    print("you can go for shopping")

elif budget>5000:
    print("you can go for a gokarting")
elif budget>2000:
    print("you can go for a movie")
else:
    print("Take rest")
'''


        
            
        
