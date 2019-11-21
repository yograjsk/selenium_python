class Animal:
    def speak(self):
        print("Animal Speaking")

class Dog(Animal):
    def speak(self):
        print("Dog is Barking")
        super().speak()

d = Dog()
d.speak()
