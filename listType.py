tes_varities = ["Black", "Green", "Oolang", "White"]
print(tes_varities)
tes_varities[3] = "Herbal"
print(tes_varities)

tes_varities[1:2] = "Lemon"
print(tes_varities) #['Black', 'L', 'e', 'm', 'o', 'n', 'Oolang', 'Herbal'] 

tes_varities[1:2] = ["Lemon"]
print(tes_varities) #['Black', 'Lemon', 'Oolang', 'White']


tes_varities[1:1] = ["Test", "Test"]
print(tes_varities) #['Black', 'Test', 'Test', 'Lemon', 'Oolang', 'White']

for tea in tes_varities:
    print(tea)
    print(tea, end="_")



# Condition in List
if "Ginger" in tes_varities:
    print("I have to payy")

tes_varities.append("Ginger")
print(tes_varities)

if "Ginger" in tes_varities:
    print("I have to payy for Ginger")


squared_num = [x**2 for x in range(10)]
print(squared_num)



# List Comprehensions 
# A Generator Expression is similar to a list comprehension, but instead of creating the entire list in memory, it generates values on the fly, one at a time, using lazy evaluation.

emails = ["alice@gmail.com", "bob@yahoo.com", "eve@outlook.com"]
domains = [email.split("@")[1] for email in emails]
print(domains)


nums = [1, 2, 3, 4, 5, 6]
evens = [n for n in nums if n % 2 == 0]
print(evens)


words = ["  Hello", "World  ", " PYTHON  "]
cleaned = [word.strip().lower() for word in words]
print(cleaned)