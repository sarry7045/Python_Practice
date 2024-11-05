# 1
class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand    # __ we can use this for private the variable , so cannot access everyone
        self.model = model
        Car.total_car += 1

    def full_Name(self):
        return f"{self.brand} {self.model}"    

   # Suppose we have to private the brand object, for that we have to create the def inside the car : Example      -     Encapsulation
    def get_brand(self):
        return self.__brand + "New One" 

    @property  # using this - hum isko override nhi krr sakte, for security purpose ex: my_car.fuel_type = Electric
    def fuel_type(self):
        return "Petrol or Diesel"   # Polymorphism

    @staticmethod   # Decorator
    def general_description():   # We dont't need self for static method
        return "Cars Transport"  


my_car = Car("Toyota", "Corolla")   
# print(my_car.__brand)         
print(my_car.model)        
print("Car - ",Car.general_description())        
# print(my_car.full_Name())



# 2
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
  
    def fuel_type(self):
        return "Electric Charge"     # Polymorphism  


my_tesla = ElectricCar("Tesla", "Model S", "100KWH")
print(my_tesla.model)       
# print(my_tesla.full_Name())       
# print(my_tesla.get_brand())   
print(my_tesla.fuel_type())   # Polymorphism
safari = Car("Tata", "Safari")
print(safari.fuel_type())
# So basically we can't access brand name direct , we have to use get_brand() function for that     -     Encapsulation
