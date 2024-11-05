
# 1
numbers = [1,-2,3,-4,5,6,-7,-8,9,10]
positive_number_count = 0
for num in numbers:
    if num < 0:
        positive_number_count += 1
print("Final Count", positive_number_count)


# 2
input_str = "teeter"
for char in input_str:
    if input_str.count(char) == 1:
        break
    print(char)  


# 3
number = 5
factorial = 1
while number > 0:
    factorial = factorial * number
    number = number - 1
    print("Facto", factorial)


# 4
items = ["apple", "banana", "orange", "apple", "mango"]
unique_item = set()

for item in items:
    if item in  unique_item:
        print("U Item", item)
        break
    unique_item.add(item)


# 5
import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attemps ", attempts + 1, "Wait Time", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
