x = 99

def func(y):
    z = x + y
    return z
result = func(1)
print(result)
# Factory functions is also kmows as Closure



def func1():
    x = 88
    def func2 ():
        print(x)
    func2()
func1()


def coder(num):
    def actual(x):
        return x ** num
    return actual
 
f = coder(2)
g = coder(3)
print(f(3))

