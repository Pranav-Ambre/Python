def sum(*args): # *args is a tuple which values pass to the sum function
    total=0
    for i in args:
        total+=i
    return total

print(sum(1,2,3,4,5))