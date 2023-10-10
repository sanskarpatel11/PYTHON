class Parent:
    def Parent_method(self):
        print("This is Parent Class Method")


class Child(Parent):
    def child_method(self):
        print("This is Child Class Method")
        super().Parent_method()

abc = Child()
abc.child_method()
