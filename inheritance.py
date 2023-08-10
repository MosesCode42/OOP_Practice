#Parent Class
class Vehicle:
    def Vehicle_data(self):
        print("Hello from the Vehicle Class")
        
#child class
class Car(Vehicle):
    def Car_data(self):
        print("Hello from the Car class!")
        
class Bike(Vehicle):
    def Bike_data(self):
        print("Hello form Bike Class!")

        
 #objects based on car       
car01 = Car()

#get vehicle data
car01.Vehicle_data()
car01.Car_data()

bike01 = Bike()
bike01.Car_data()
