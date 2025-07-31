import time


# 1
def greet_decorator(func):
    def wrapper():
        print("Hello!")
        func()
        print("Goodbye!")
    return wrapper

@greet_decorator
def say_name():
    print("My name is Suraj")

say_name()
# Equivalent Without @ Syntax
# say_name = greet_decorator(say_name)
# say_name()



# 2
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}run in {end - start} time")
        return result
    return wrapper

@timer     # Decorator - Means jab bhi iss function ko chalna hoga woh iss function se hoke he gujrega
def example_function(n):
    time.sleep(n)

example_function(2)



# 3
def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper (*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper


@cache
def long_running_functon(a, b):
    time.sleep(4)
    return a + b

print(long_running_functon(2,3))
print(long_running_functon(4,3))
