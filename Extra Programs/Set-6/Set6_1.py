a=int(input("Enter first number::"))
b=int(input("Enter second number::"))
print("Before swapping A=",a,"B=",b)
if(a%2==0 and b%2==0):
    t=a
    a=b
    b=t
print("After swapping A=",a,"B=",b)

