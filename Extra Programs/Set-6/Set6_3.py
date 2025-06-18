x1,y1,x2,y2=[int(x) for x in input("Enter Co-Ordinates::").split()]
if(y1==y2):
    print("Given points are parallel to X-axis")
    import math
    dist=math.pow((x1-x2),2)
    print("Distance between the points are :",dist)
else:
    print("The points are not parallel to X axis")
    
    