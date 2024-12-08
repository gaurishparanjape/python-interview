class Test:

    __private_var = 10

    _protected_var = 20

    def method(self):
        print(Test.__private_var + Test._protected_var)

t_obj = Test()

print(Test._protected_var)
#print(Test.t_obj.__private_var)
t_obj.method()