class emp:
    comp="HP"
    def __init__(self,sal,name,bond,comp):
        self.sal=sal
        self.name=name
        self.bond=bond
        self.comp=comp
    
    def info(self):
        print(f"The salary of employee is {self.sal}. The name is {self.name}. The bond is {self.bond}")
    
obj=emp(340000,"Sai",3,"ASUS")
print(obj.comp)
print(emp.comp) # For printing the comp="HP"

