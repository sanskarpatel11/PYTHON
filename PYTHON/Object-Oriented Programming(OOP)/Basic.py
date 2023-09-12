class student:
    name = "Divyam"
    age = 9
    
    def info(self):
        print (f"{self.name} is {self.age} Year old")

a = student()


b = student()
b.name = "Sanskar"
b.age = 14
b.info()
c = student()
c.name = "Rahul"
c.age = 15
c.info()
d = student()

d.info()

# Output

#Sanskar is 14 Year old
#Rahul is 15 Year old
#Divyam is 9 Year old