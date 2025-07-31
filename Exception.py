# try:
#     # Code that may raise an exception
# except SomeException:
#     # What to do if exception occurs
# else:
#     # Run if no exception occurred
# finally:
#     # Always run, whether exception occurred or not


# | Exception           | Occurs When...                               |
# | ------------------- | -------------------------------------------- |
# | `ZeroDivisionError` | Dividing by zero                             |
# | `ValueError`        | Invalid type for operation (e.g. int("abc")) |
# | `TypeError`         | Wrong type used (e.g. add str + int)         |
# | `IndexError`        | Index out of range in list                   |
# | `KeyError`          | Missing key in dictionary                    |
# | `FileNotFoundError` | File path doesn't exist                      |

try:
    a = 10
    b = 0
    result = a / b
except ZeroDivisionError:
    print("Cannot divide by zero.")


try:
    age = int(input("Enter your age: "))  # Input "twenty"
except ValueError:
    print("Please enter a valid number.")


items = ["apple", "banana"]
try:
    print(items[5])
except IndexError:
    print("Item not found in list.")


person = {"name": "Suraj"}
try:
    print(person["age"])
except KeyError:
    print("Key not found in dictionary.")


try:
    with open("data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found. Please check the path.")


# else and finally
try:
    num = int(input("Enter a number: "))
    print("Half of the number:", num / 2)
except ValueError:
    print("That was not a number.")
else:
    print("Success! No errors.")
finally:
    print("This always runs.")


# Custom Exceptions

    class TooYoungError(Exception):
     pass

age = 15
try:
    if age < 18:
        raise TooYoungError("You must be 18+ to register.")
except TooYoungError as e:
    print("Custom Error:", e)
