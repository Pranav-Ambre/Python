a=int(input("Enter the first number::"))
b=int(input("Enter the second number::"))
c=int(input("Enter the third number::"))
big=0
if(a>b and a>c):
    big=a
elif(b>c and b>a):
    big=b
else:
    big=c
print("Biggest number is:::",big)
