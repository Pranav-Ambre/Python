def mark(**kwargs):
    for i in kwargs.keys():
        print(f"The marks of {i} is {kwargs[i]}")

mark(A=90,B=60,C=80,D=97)