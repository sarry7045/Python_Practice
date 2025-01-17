types = {"Masala" : "Spicy", "Ginger" : "Zesty"}
print(types["Masala"])


for chai in types:
    print(chai)
    print(types[chai])


for key, value in types.items():
    print(key)
    print(value)


if "Masala" in types:
    print("Yess i am here")


types["Chasa"] = "Milk"
print(types)
print(types.pop("Masala"))
print(types)

del types["Ginger"]
print(types)


teaShop = { "chai": {"Masala":"Spicy", "Ginger":"Zesty"}, 
             "Tea": {"Green" :"Mild", "Black": "Strong"}
             }
                     
print(teaShop)
print("TeaShop", teaShop["chai"]["Masala"])



squared_num = {x:x**2 for x in range(6)}
print(squared_num)


key=["A", "B", "C"]
default_value = "123"
new_dict = dict.fromkeys(key, default_value)
print(new_dict)
