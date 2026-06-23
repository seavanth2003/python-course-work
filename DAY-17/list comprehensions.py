#list comprehension's
'''
res1=[]
for i in range(1,11):
    res1.append(i)
res2=[i for i in range(1,11)] # list comprehension

print(res1)
print(res2)

res3=[]
for i in range(3,31,3):
    res3.append(i)
res4=[i for i in range(3,31,3)]

print(res3)
print(res4)

res5=[]
for i in range(2,51,2):
    res5.append(i)

res6=[i for i in range(2,51,2)]
print(res5)
print(res6)
'''

'''
a='python programming'
l=[]
for i in a:
    if i in 'aeiouAEIOU':
        l.append(i)
print(l)

l1=[i for i in a if i in 'aeiouAEIOU'] #list comprehension
print(l1)
'''

'''
a=[1,2,4,5,6,7,8,10,20,46,80]
l=[]
for i in a:
    if i%2==0:
        l.append(i)
    else:
        l.append(0)
print(l)

l1=[i if i%2==0 else 0 for i in a]
print(l1)
'''
#conditions
'''
l=[val for var in seq]
l=[val for var in seq if condition]
l=[val if condition else val for var in seq]
'''
'''
l=[int(input(f"Enter the number-{i+1}: "))for i in range(10)]
print(l)
'''
'''
l=[]
for i in range(3):
    for j in range(1,4):
        l.append(j)
print(l)

l1=[j for i in range(3) for j in range(1,4)]
print(l1)
'''
'''
l=[[j for j in range(1,4)]for i in range(3)]
print(l)
'''
'''
s=set()
for i in range(1,11):
    s.add(i)

s1={i for i in range(1,11)}
print(s,s1)
'''

'''
res={i:i*i for i in range(1,11)}
print(res)
'''
'''
res={input("Enter the name: "): int(input("Enter the mark: "))for i in range(5)}
print(res)
'''
