class Example:
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def class_method(cls):
        print("This is a class method")
        print(f"Accessing class variable: {cls.class_variable}")

# Create an instance of Example and rename it to 'name'
name = Example("I am an instance variable")

# Call the class method on the class itself
Example.class_method()

# You can also call the class method on an instance
name.class_method()
