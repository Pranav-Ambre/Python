class Animal:
    def __init__(self,name):
        self.name=name
    
    def speck(self):
        print("Speaking.......")

class dog(Animal): # Inhereting the perent class properties
    def speck(self):
        super().speck() #Calling a parent class method
        print("Woof!")

obj=dog("Dog")
obj.speck()