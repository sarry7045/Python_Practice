# An iterator is an object that implements two methods:

# __iter__() → returns the iterator object itself

# __next__() → returns the next item from the collection. When there are no more items, it raises StopIteration.

# It's cannot perform Reverse

my_list = [1,2,3,4,5]

it = iter(my_list)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

while True:
    try:
        fruit = next(it)
        print(fruit)
    except StopIteration:
        break