class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,p):
        return Point((self.x+p.x),(self.y+p.y))
    
    def show(self):
        print(f"X is {self.x} and Y is {self.y} ")

p1=Point(2,3)
p2=Point(6,5)

p=p1+p2
p.show()