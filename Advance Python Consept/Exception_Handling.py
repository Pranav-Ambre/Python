while True:
    try:
        a=int(input("Enter the number 1: "))
        b=int(input("Enter the number 2: "))

        print(f"Addition is: {a+b}")
    except Exception as e:
        print("Some error is occurs",e)
    
    finally: 
        print("This is always executed.....")