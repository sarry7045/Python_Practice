# 1
def sqaure_of_num(number):
    return number ** 2
print(sqaure_of_num(3))  



# 2
def greet(name="Yadav"):
    return "Hello" + name + "!"
print(greet("Suraj")) # If we don't provide any value in argument, then it's automatically take default value = "Yadav"



# 3 - Annonymus / Lamba - Function
cube = lambda x: x * 3
print(cube(3))



# 4
def summ_all(*args): # * means it's ready for the multiple arguments
    return sum(args)
print(summ_all(1,2))
print(summ_all(1,2,3,4))



# 5
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_kwargs(name = "Suraj", surname= "Yadav")
print_kwargs(name = "Suraj", surname= "Yadav", adress= "Mumbai")



# 6
def even_generator (limit):
    for i in range(2, limit + 1, 2):
        yield i        # yield is use for ki, function pichla value kya return kiya the woh memory me save krke rakhata hai
         
for  num in even_generator(10):
    print("num", num)



# 7
def factorial (n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1) # Recursive function - function k undar wahi same function use krna