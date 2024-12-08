def outer_function1(msg):
    def inner_func():
        print("Inner function message,", msg)

    return inner_func()


outer_function1("No1: Hey")
print("=="*1000)

# Let's execute the above code without executing the inner function

def outer_function2(msg):
    def inner_func():
        print("Inner function message,", msg)

    # this will return the inner function waiting to be executed.
    return inner_func
# You will not getting any output by running below line as inner function is not yet executed and it is waiting to get executed.
# outer_function("Hey")

# Hence we need to assign it to a variable and call that variable so that inner function gets executed.

call_func = outer_function2("No2: Hey")
call_func()

print("=="*1000)
"""
Decorator is a function which takes another function as an argument, add some kind of functionality, and returns another function

ALl of this without altering the source code of the original function.
"""
#Lets say instead of printing the message, we execute a function that we passed.
def outer_function3(original_func):
    def inner_func():
        return original_func()
    return inner_func

def display():
    print("Display function ran")
"""
decorated_display() function is equal to the inner function which is waiting to be executed, and when executed it runs the original function(which is display()).
"""
decorated_display = outer_function3(display)
decorated_display()
print("=="*1000)
#The above code is same as below code

def decorator_function(original_func):
    def wrapper_func():
        print("Executing inner function.")
        return original_func()
    return wrapper_func
@decorator_function
def display():
    print("This is from display function")

display()

print("=="*1000)


def decorator(function):
    def inner(a,b):
        if b ==0:
            print("Hey bro rerun the program, as b=0")
            return
        return function(a,b)
    return inner
@decorator
def div(a,b):
    return a/b

print(div(4,4))
print(div(2,0))