def greater(x):
    if(x>9):
        return True
    else:
        return False
    
a=[1,2,3,33,44,11,3,4,55,45,23,5,2,455,323,324]

new=list(filter(greater,a))
print(new)