"""
Decorators modifies the behaviour of a function or a class.
- A function in python can be used as arguments.
- A function is a instance of object
- We can store the function as a parameter
- We can pass the function to another function
- We can return a function from another function.
- We can even store the function in a list or other data types.
"""

# Treating functions as objects
def shout(text):
    return text.upper()
print(shout("hello"))
yello = shout
print(yello('yello'))



#Passing the function as a argument
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    greeting = func("Hey I am here to get passed as an argument")
    print(greeting)

greet(shout)
greet(whisper)

#Returning function from another function
def create_adder(x):
    def addy(y):
        return x+y
    return addy
add_15 = create_adder(10)
print(add_15(15))

#Decorators
def decorator(func):
    def inner(a, b):
        if b == 0:
            print("b cannot be zero")
            return
        return func(a,b)
    return inner
@decorator
def div(a,b):
    print(a/b)
div(1,0)
div(4,2)


#Example 2
def greet_CEO(func):
    def inner(name):
        if name == "Gaurish":
            print("We are blessed to have you.")
        return func(name)
    return inner

@greet_CEO
def name_greet(name):
    print("Hello, Welcome to our restaurant ", name)

name_greet("sampan")
name_greet("Gaurish")