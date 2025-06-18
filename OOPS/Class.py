class Emp:
    company="HP"

    def sal(self): #self is important to here because self is way to reference the object of which has being created
        return 1000000

obj= Emp()
print(obj.sal())
print(obj.company)

obj1= Emp()
print(obj1.sal())
print(obj1.company)