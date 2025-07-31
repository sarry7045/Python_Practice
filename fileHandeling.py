# file = open("info.txt", "r")
# content = file.read()
# print(content)
# file.close()

with open("info.txt", "r") as filee:
    content = filee.read()
    print(content)

# file = open("info.txt", "w")
# file.write("Heey Testing")
# file.close()


# file = open("info.txt", "a")
# file.write("Heey Testing I am Suraj")
# file.close()
