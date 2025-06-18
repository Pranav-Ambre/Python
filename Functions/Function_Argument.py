def add1(a1,b1):
    x1=a1+b1
    return x1

c1=add1(20,30)
print(c1)

#Default argument
def add(a,b,pl=0): 
    x=a+b+pl
    return x

c=add(10,20)
print(c)

#Keyword argument
def var(p,q):
    v=p+q
    return v

dd=var(q=10,p=70)
print(dd)