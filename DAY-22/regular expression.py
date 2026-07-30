'''
import re

#pattern='[abc]'
pattern='[a-z]'
text='codegnan'


res=re.match(pattern,text)
print(res.group() if res else "No Match Found")
'''

'''
import re

pattern='[a-z]'
text='python version 3.11'

res=re.search(pattern,text)
print(res.group() if res else "No Match Found")'''

'''
import re

pattern='[0-9]'
text='python version 3.11'

res=re.findall(pattern,text)
print(res)
'''

'''
import re

#pattern='[0-9]'
pattern='[a-z]'
text='python version 3.11'

res=re.finditer(pattern,text)

for i in res:
    print(i.group(),i.start())
    '''

'''
import re

pattern='[0-9]{9}' #{}-->it acts as length of a text
text='987654321'
res=re.fullmatch(pattern,text)
print(res.group() if res else "No Match Found")
'''
'''
import re
pattern=r'[,a+yn]'
text='java,python,c++'
res=re.split(pattern,text)
print(res)'''

#sub->replace function
import re

pattern=r'[0-9]{2}'
text='python:34 mysql:78 java:55 html:45'

res=re.sub(pattern,'**',text)
print(res)



    
