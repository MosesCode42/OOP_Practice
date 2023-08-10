class Person:
    def __init__(self, name, age, personID):
        self.name = name
        self.age  = age
        self.personID = personID
        
    def display_data(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Person ID: {self.personID}")
        
        
person1 = Person('Moses', 30, 42)
person2 = Person('Jacky', 25, 11)
person3 = Person('Nathan', 8, 99)

print("---------------------")
print(person2.name)
print(person2.age)
print(person2.personID)
print("----------------------")

print(person3.name)
print(person3.age)
print(person3.personID)
print("----------------------")

print(person1.name)
print(person1.age)
print(person1.personID)
print("----------------------")

print(person1.display_data())
print("----------------------")
print(person2.display_data())
print("----------------------")
print(person3.display_data())
    
    