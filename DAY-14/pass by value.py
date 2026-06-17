'''pass by value and pass by refernece'''

#int float complex str list tuple  set dict bool
#diff int float complex str tuple bool
#same list set dict

def update(n):
    n.count(8)
    print("Inside:",n)

n=(1,2,3,4,5,6,7)
update(n)
print("Outside:",n)

