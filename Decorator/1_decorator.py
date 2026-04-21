def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper


@my_decorator
def say_hello():
    print("Hello")


say_hello()

#  👉 Decorator is used to add extra functionality to a function without modifying its original code.