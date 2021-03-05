# Create the logging_decorator() function 👇
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"You called {func.__name__}{args}")
        result = func(args[0], args[1], args[2])
        print(f"It returned: {result}")

    return wrapper


# Use the decorator 👇

@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(1, 2, 3)

