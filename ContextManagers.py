# Context Managers comes in the picture to Manage Memory in better way.
# with Keyword is use for Cleanup Operations and Resource Management

file = open("text.txt", "r")
content = file.read()
file.close()

# When we use Context Manager.
# If we dont want to use try catch then we can directly use CM like this:
with open("text.txt", "r") as file:
    content = file.read()
    print(content)