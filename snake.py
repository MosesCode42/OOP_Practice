class Snake:
    def __init__(self, name):
        self.name = name
        
    def display(self):
        print(f"Snake name: {self.name}")
        
    def harmful(self):
        print(f"Both {snake01.name} and {snake02.name} are harmful")
    
    def modifyName(self, new_name):
        self.name = new_name
        
snake01 = Snake('Anaconda')
snake02 = Snake('Python')

print(snake01.display())
print(snake02.display())

print(snake01.harmful())

snake01.modifyName('Cobra')
print(snake01.name)
snake02.modifyName("Black Mamba, Kobe(rip)")
print(snake02.name)

 



