class Animal: 
    locaation="Austria"

    def __init__(self,name):
        self.name=name

    def speak(self):
        print("Speaking now")

# a=Animal("Dog")
# a.speak()

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof")


d=Dog("Bruno")
d.speak()
print(d.locaation)
    