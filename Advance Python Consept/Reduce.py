from functools import reduce
number=[10,20,30,40,50,60,70,80,90]

def sum(a,b):
    return a+b

new=reduce(sum,number)
print(new)