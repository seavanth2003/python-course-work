'''
status=None
assert status !=None, "you need to update the status"
print(status)
''' 
#assertions is the debugging tool'
'''
name='abc'
batch=55
age=21
assert(name !=None and batch !=None and age !=None),"You need to update the data"
print(name,batch,age)
'''

#While loop
'''
i=1
while i<11:
    print(i)
    i+=1
    '''
'''
i=2
while i<21:

    print(i)
    i+=2
    '''
'''
i=10
while i>0:
    print(i)
    i-=1
    '''
'''
i=5
while i<51:
    print(i)
    i+=5
    '''
'''
l=[1,2,4,5,6,7,3,9]
i=0
while i<len(l):
    print(l[i])
    i+=1
    '''
moves=30
while moves>1:
    status=input("[w]in or [c]ontinue: ").upper()
    if status =='w':
        print("you won the game")
        break
    moves-=1
    print(f'{moves} moves are left')

else:
    print("Game over")

