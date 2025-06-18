class Employee:
    company="HP"
    
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    
    #Instance Method 
    def show(self):
        info=f"The name is {self.name} and a salary is {self.sal}"
        print(info)
    
    #Static Method
    @staticmethod
    def sum(a,b):
        return a+b
    
    #Class Methods

    @classmethod
    def print_comp(cls):
        print(cls.company)
    
    @classmethod
    def change_comp(cls,new_comp):
       cls.company=new_comp
    
e=Employee("ABC",13214)
e.show()
e.print_comp()
e.change_comp("ASER")
e.print_comp()
print(e.sum(10,20))
    

