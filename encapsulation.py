class Employee:
    def __init__(self, name, salary, project):
        self.__name = name 
        self._salary = salary
        self.project = project
        
    #show the employee data
    def show_details(self):
        print(f"The name is {self.__name} and the Salary is {self._salary}")
        
    #show project details
    def work(self):
        print(f"{self.__name} and is working on {self.project}")
        
        
#Objects for employee
emp1 = Employee("Jacky", 900000, "Convergence Law & Tech")

#Access public name
#print(f"The value of name is {emp1.__name}")

emp1.show_details()
emp1.work()
        
        
     