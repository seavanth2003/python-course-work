#recursion

'''def func()   (syntax)
if basecondi:
    return
func()
'''

'''
def func(num):
    if num==0:
        return
    func(num-1)
    print(num,end=' ')
    #func(num-1)
    

func(5)
'''

'''
def sumofdigits(n):
    if n==0:
        return 0
    return n+sumofdigits(n-1)
print(sumofdigits(20))
'''

'''
def sumofdigits(n): (product of sum)
    if n==1:
        return 1
    return n*sumofdigits(n-1)
print(sumofdigits(5))
'''

'''
def power(base,pow):
    if pow==0:
        return 1
    return base*power(base,pow-1)
print(power(2,5))
print(power(3,8))
'''
'''
def reverseofstr(s):
    if len(s) == 0:
        return s
    else:
        return reverseofstr(s[1:]) + s[0]

print(reverseofstr("python"))
'''

def reverseofstr(s,ind):          (reverseof string)
    if ind==0:
        return s[0]
    return s[ind]+reverseofstr(s,ind-1)
l="python programming"
print(reverseofstr(l,len(l)-1))

