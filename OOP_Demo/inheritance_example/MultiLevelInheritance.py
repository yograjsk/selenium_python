class Animal:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def speak(self):
        print("Speaking....")

class Dog(Animal):
    # def __int__(self,a,b,x):
    #     self.a = a
    #     self.b = b
    #     self.x = x

    def __init__(self,a,b,x):
        Animal.__init__(self, a,b)
        self.x = x

    def bark(self):
        print(self.a,"and",self.b,"and",self.x,"are Barking...")

d = Dog("dog1","dog2","dog3")
d.bark()
d.speak()
