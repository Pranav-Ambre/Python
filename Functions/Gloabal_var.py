def add(a,b):
    c=a+b
    global z
    z=0
    return c

z=10
print(add(10,20))
print(z)

