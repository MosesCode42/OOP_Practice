class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age #private member
        
    #getting age
    def get_age(self):
        return self.__age
    
    #setting age
    def set_age(self, age):
        self.__age = age
        
person01 = Person("Jonas", 10)

print(f"Name: {person01.name}, Age: {person01.get_age()}")

#Modify age
person01.set_age(3)

#Getting private age for person01 after modification
print(f"Name: {person01.name}, Age: {person01.get_age()}")



        