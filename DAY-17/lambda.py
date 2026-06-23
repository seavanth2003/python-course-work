#map(dict)
'''
d={'sugar':40,'milk':50,'honey':90,'salt':100}
res=dict(map(lambda i:(i[0],i[1]+i[1]*0.18),d.items()))
res1=dict(map(lambda i:(i[0],i[1]-i[1]*0.5),d.items()))
print(res)
print(res1)
'''
#filter(dict)
d={'sugar':40,'milk':50,'honey':90,'salt':100}
res=dict(filter(lambda i:i[1]>50,d.items()))
res1=dict(filter(lambda i:i[1]<50,d.items()))
print(res)
print(res1)
