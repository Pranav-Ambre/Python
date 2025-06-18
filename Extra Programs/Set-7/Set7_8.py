a=int(input("Enter the first number::"))
b=int(input("Enter the second number::"))
c=int(input("Enter the third number::"))
d=int(input("Enter the fourth number::"))
big=0
if(a>b and a>c and a>d):
    big=a
elif(b>c and b>a and b>d):
    big=b
elif(c>a and c>b and c>d):
    big=c
else:
    big=d
print("Biggest number is:::",big)
