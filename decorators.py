import time

# 1
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}run in {end - start} time")
        return result
    return wrapper

@timer     # Decorator - Means jab bhi iss function ko chalna hoga woh iss function se hoke he gujreja
def example_function(n):
    time.sleep(n)

example_function(2)



# 2
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
