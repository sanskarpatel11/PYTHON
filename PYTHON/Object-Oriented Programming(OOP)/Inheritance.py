class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
      
        print(f"{self.name} is {self.age} years old")
class Person0(Person):
    def show(self):
        print("Hello World")
   


a = Person("sanskar patel", 14)
a.info()
b = Person("rohuit",18)
c= Person0("Rahul",18)
b.info()

c.show()
