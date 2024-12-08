#Static Variable

class TestClass:
    a = 10

    def __init__(self):
        print(self.a)
        TestClass.b = 20
        print(TestClass.a)
        print(TestClass.b)

    def method(self):
        print(self.a)
        print(TestClass.a)

    @classmethod
    def classMethod(cls):
        print(cls.a)
        print(TestClass.a)

    @staticmethod
    def statMethod():
        print(TestClass.a)

#To update static variable use the className or cls variable and not self or object

#We cant Update static variable with self or object reference, if we do, then a new object reference will be created.

class B:
    static_var = 10

    def instance_method(self):
        self.static_var = 100



t = B()
t.instance_method()
print(B.static_var)
print(t.static_var)



