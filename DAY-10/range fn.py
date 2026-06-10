#str list tuple set dict range()

'''
for var in seq:
    print(var)
'''

'''
s='python programming'
for ch in s:
    print(ch)
    '''

'''
l=['sugar','salt','oil','eggs']
for item in l:
    print(item)
    '''
'''
t=('1.intro','2.Tokens','3.datatypes')
for i in t:
    print(i)
'''
'''
s={'laptop','mouse','keyboard','phone','charger'}
for i in s:
    print(i)
 '''   '''

d={'name':'subbu','batch':37,'course':'PFS','skills':['python','Html','CSS']}
for i in  d:
    print(i,d[i])
    '''

#range(start,stop+1,step) =>(0,n,1)
'''
for i in range(1,11):
    print(i)
for i in range(2,51,2):
    print(i)
for i in range(5,101,5):
    print(i)
for i in range(20,0,-1):
    print(i)
    '''
'''
for i in range(6):
    print(i)
   '''
'''
for i in range(1,100,2):(odd)
    print(i)

for i in range(0,50,2):(even)
    print(i)
    '''
'''
s='control statements'
for i in range(len(s)):
    print(i,s[i])
    '''
'''
k=(4,2,7,9,4,2,5)
for i in range(len(k)):
    print(i,k[i])
   '''
# Enumerate functions
'''
s='looping'
for i in enumerate(s):
    print(i[0],i[1])
   '''
'''
k=(5,48,1,4,6,9)
for i in enumerate(k):
    print(i[0],i[1])
    '''
'''
t=(4,8,3,9,1,0,2)
for i in enumerate(t):
    print(i[0],i[1])

k=(3,5,6,7,8,9,1,0)
for i in enumerate(t):(it prints both t&k)
    print(i[0],i[1])
'''

'''
for i in range(10):
    if i ==5:
        break
    print(i)
 '''
'''
for i in range(10):
    if i==6:
        continue
    print(i)
    '''
'''
s='control statements'
for i in s:
    if i in 'AEIOUaeiou':
        print(i)
        '''
'''

k=(45,26,54,93,98,29,10,68,36)
for i in k:
    if i%2==0:
        print(i)
        '''

d={'laptops':0,'chargers':2,'keyboard':20,'phone':18,'mouse':9}
for i in d:
    if d[i]:
        print(i)

