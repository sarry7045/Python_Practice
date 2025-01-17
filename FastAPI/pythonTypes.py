def add(firstName: str | None, lastName: str = None):
    if(firstName != None):
        firstName.capitalize()
    return firstName + " " + lastName


FirstName = "Suraj"
LastName = "Yadav"


name = add(FirstName, LastName)
print(name)
