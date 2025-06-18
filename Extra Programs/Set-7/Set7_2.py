a=int(input("Enter the first side::"))
b=int(input("Enter the second side::"))
c=int(input("Enter the third side::"))
if(a == b and b == c):
    print("EQUILATERAL TRAINGLE")
elif (a == b or b == c or a == c):
    print("ISOSCELES TRAINGLE")
else:
    print("SCALENE TRAINGLE")
