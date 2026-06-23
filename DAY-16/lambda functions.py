#lambda functions

'''
add=lambda a,b:a+b
print(add(18,22))
print(add(100,200))
'''


'''
square=lambda x:x*x
print(square(4))
print(square(5))
'''

'''
wish=lambda name:f" Mr {name} welcome to codegnan"
print(wish('sujith'))
print(wish('pradeep'))
'''


'''
gst=lambda price:price+price*0.18
print(gst(74900))
print(gst(7700))
'''
'''
greatest=lambda a,b:a if a>b else b
print(greatest(298,980))
print(greatest(100,120))
print(greatest (899,898))
'''

'''
iseven=lambda a:f"{a}-Even number" if a%2==0 else f"{a}-odd number"
print(iseven(3))
print(iseven(8))
print(iseven(100))
'''

'''
l=[1,2,3,4,5,6,7]
res=list(map(lambda i:i**3,l))
print(res)
'''

'''
names=['subbu','ranjith','praneeth']
t=list(map(lambda i:i.title(),names))
print(t)
'''

'''
l=[1,2,3,4,5,6,7,8,9]
res=list(filter(lambda i:i%2==0,l))
print(res)

l=[1,2,3,4,5]
res=list(filter(lambda i:i>5,l))
print(res)

n=[1,2,3,4,5,6,7]
res=list(filter(lambda i:i%3==0,n))
print(res)
'''

'''
from functools import reduce

l=[1,2,3,4,5,6,7,8,9,10]
s=reduce(lambda sum,i:sum+i,l)
p=reduce(lambda pro,i:pro*1,l)
m=reduce(lambda max,i:max if max>i else i,l)
mi=reduce(lambda max,i:max if max<i else i,l)

print(s,p,m,mi)
'''

d={'sukumar':50,'rohith':40,'nagraj':60,'dinakar':80,'saketh':70}
print(dict(sorted(d.items())))
print(dict(sorted(d.items(),key=lambda i:i[1])))

print(dict(sorted(d.items(),reverse=True)))
print(dict(sorted(d.items(),key=lambda i:i[1],reverse=True)))
