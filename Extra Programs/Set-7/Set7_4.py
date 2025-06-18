x = float(input("Enter the x-coordinate of the point: "))
y = float(input("Enter the y-coordinate of the point: "))

if x > 0 and y > 0:
    print("The point is in Quadrant I")
elif x < 0 and y > 0:
    print("The point  is in Quadrant II")
elif x < 0 and y < 0:
    print("The point is in Quadrant III")
elif x > 0 and y < 0:
    print("The point is in Quadrant IV")
elif x == 0 and y != 0:
    print("The point lies on the y-axis")
elif x != 0 and y == 0:
    print("The point lies on the x-axis")
else:
    print("The point is at the origin (0, 0)")
