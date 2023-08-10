#Person parent class
class Person:
    def person_data(self, name, age):
        print("Hello from the Person class!")
        print(f"The name is {name}, and the age is {age}")
        
#Company parent class
class Company:
    def company_data(self, comp_name,location):
        print("Welome to the company!")
        print(f"The company name is {comp_name} and location is {location}")
        
#Employee child class
class Employee(Person, Company):
    def employee_data(self, salary, skill):
        print("Welcome to the Employee class")
        print(f"Salary is {salary} and Skill is {skill}")
        
        
#Objects for employee
emp01 = Employee()

#Get data on screen
emp01.person_data("Moses", 35)
emp01.company_data("Google", "Westlands")
emp01.employee_data("600000", "AIMLE")

