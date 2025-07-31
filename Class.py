class Person:
    name = "Suraj"
    occupation = "Software Developer"
    networth = 10

    def info(self):
        print(f"{self.name} is a {self.occupation}")


abc = Person()
abc.name = "Yadav"
abc.occupation = "Full Stack Developer"

abc.info()


# Lets suppose we want to make a copy of class and use of it - Inheritance
class Programmer(Person):
    def showLanguage(self):
        print("Heyy")

abc1 = Programmer()

# There are mutiple inheritance - Single Inheritance, Multiple Inheritance, Multilevel Inheritance