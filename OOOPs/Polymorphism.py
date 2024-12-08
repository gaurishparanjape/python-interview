#Operator Overloading# add and multiply operator

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages
b1 = Book(100)
b2 = Book(200)
print(b1+b2)

#Method Overloading using inheritance

class Parent:

    def BE(self):
        print("Parent BE")


class Child(Parent):

    def BE(self):
        print("Child BE")


child_obj = Child()
child_obj.BE() # This is compile time polymorphism, object is declared of child and method that is getting called is of the child itself.

parent_obj = Parent()
parent_obj.BE()


child_obj_2 = Child()
child_obj_2

