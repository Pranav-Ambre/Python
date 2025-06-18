sal=int(input("Enter the salary:"))
if(sal<15000):
    print("PEON")
elif(sal>=15001 and sal<=25000):
    print("2nd Division Clerk")
elif(sal>=25001 and sal<=35000):
    print("1st Division Clerk")
elif(sal>=35001 and sal<=45000):
    print("Assistant Manager")
elif(sal>=45001 and sal<=60000):
    print("Manager")
else:
    print("Invalid salary")