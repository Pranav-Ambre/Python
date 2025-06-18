class emp:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    
    def __str__(self):
        return f"The name is {self.name} and salary is {self.sal}"
    
    def __repr__(self):
        return f"Name: {self.name} Salary: {self.sal}"
    
    def __len__(self):
        return len(self.name)

e=emp("Pranav",10000000)
print(len(e))
print(e.name,e.sal)
print(str(e))
print(repr(e))
