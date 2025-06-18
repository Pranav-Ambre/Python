a=int(input("Enter a number between 1 to 10"))

match (a):
    case 3:
        print("You won a car")
    case 6:
        print("You won $3")
    case 7:
        print("You won a laptop")
    case _:  #.....................................defualt case
        print("Better luck next time....")