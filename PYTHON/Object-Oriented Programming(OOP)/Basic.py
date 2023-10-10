class student:
    name = "Divyam"
    age = 9
    
    def info(self):
        print (f"{self.name} is {self.age} Year old")

a = student()


b = student()
b.name = "rishab"
b.age = 14
b.info()
c = student()
c.name = "Rahul"
c.age = 15
c.info()
d = student()

d.info()

# Output

#Risbab is 14 Year old
#Rahul is 15 Year old
#Divyam is 9 Year old

class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y


a = Shape(4,3)
print  (a.area())

b = Shape(3,6)
print (b.area())

#Output

#12
#18
