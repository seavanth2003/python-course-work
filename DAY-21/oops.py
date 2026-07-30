#class,instances,object,static-> methods
'''
class Flipkart:
    discount=20
    products=['laptop','mouse','phones','keyboards']

    @classmethod
    def showproducts(cls):
        print(cls.products)

    def login(self,username,password):
        self.username=username
        self.password=password
        print(f"welcome to Flipkart {self.username}")

    @staticmethod
    def banner():
        print("20% discount is going on flipkart,shop now on")
        

praveen=Flipkart()
praveen.login('praveen','praveen@345')
praveen.banner()
praveen.showproducts()

Flipkart.showproducts()
Flipkart.banner()'''


#Encapsulation
'''
class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.followers=[]
        print(f"welcome to the Instagram,{self.username}")

vamsi=Instagram('vamsi','vamsi@123')
'''

class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.followers=[]
    def getpassword(self):
        return self.password
    def setpassword(self,newpassword):
        self.password=newpassword

vamsi=Instagram('vamsi','vamsi@123')
print("Before username:",vamsi.username)
vamsi.username='pradeep'
print("After username:",vamsi.username)
print("Before password:",vamsi.getpassword())
vamsi.setpassword('praneeth@123')
print("After password:",vamsi.getpassword())

        


