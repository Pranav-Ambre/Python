class emp:
    def __init__(self,sal,name,bond):
        self.sal=sal
        self.name=name
        self.bond=bond
    
    def info(self):
        print(f"The salary of employee is {self.sal}. The name is {self.name}. The bond is {self.bond}")
    
obj=emp(340000,"Sai",3)
obj.info()