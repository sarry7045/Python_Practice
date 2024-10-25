# 1
age = 18

if age < 18:
    print("Child")
elif age > 18:
    print("Adult")
else:
   print("None")



# 2
age1 = 24
day = "Sunday"
price = 12 if age>=18 else 8

if day == "Sunday": 
    price = price - 2
print("Ticket Price is", price)



# 3
score = 101

if score >= 101:
    print("Score is not more then 100")
    # exit()      
elif score >=80:
    print("Good")
elif score >=60: 
    print("Decent")
elif score <= 35:
    print("Fail")  



# 4
order_size = "Medium"
extra_chiz = True

if extra_chiz:
    burger = order_size + " Burger with extra Cheese"
else:
    burger = order_size + "Burger"

print(burger)



# 5
year = 2024
if (year % 400 == 0) or (year%4 == 0 and year % 100 != 0):
    print(year , "Is a Leap Year")
else:
    print(year, "Is Not a Leap Year")