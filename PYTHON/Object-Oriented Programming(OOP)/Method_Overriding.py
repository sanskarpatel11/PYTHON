class Shape:
    def area(self):
        pass

class rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

class circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    

a = circle (79)
print(a.area())
b = rectangle(20,70)
print(b.area())

c = circle(49)
print (c.area())

d = rectangle(20,10)
print (d.area())