class Student:
    standard = 1
    rollno = 1
    def __init__(self,name):
        self.name = name
        self.age = 12
        self.rollno += 1

    def show(self):
        print(f"{self.name} is {self.age} he study in class {self.standard} and hi roll.no is {self.rollno}")



st1 = Student("Rohit")

st1.standard = 6
st1.show()


st2 = Student("Rahul")
st2.standard = 12
st2.age = 17
st2.show()