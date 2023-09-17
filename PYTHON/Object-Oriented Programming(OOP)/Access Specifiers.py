class Person:
    def __init__(self, name):
        self._name = name  # Protected attribute

    def introduce(self):
        return f"Hi, I'm {self._name}!"  # Public method

class Student(Person):
    def __init__(self, name, student_id):
        Person.__init__(self, name)  # Calling the parent class constructor
        self.student_id = student_id  # Public attribute

    def study(self):
        return f"{self._name} is studying."  # Public method

# Creating a Person
alice = Person("Rohit")
print(alice._name)         # Accessing a protected attribute
print(alice.introduce())   # Calling a public method

# Creating a Student
bob = Student("Rishab", "S12345")
print(bob._name)           # Accessing a protected attribute inherited from Person
print(bob.student_id)      # Accessing a public attribute specific to Student
print(bob.introduce())     # Calling a public method inherited from Person
print(bob.study())         # Calling a public method specific to Student
