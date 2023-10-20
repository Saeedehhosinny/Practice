print("Hello, we are here to prove with your help whether the size of the sides we have indicates a triangle or not, so answer the following questions:")
a = int(input("Enter the first side:"))
b = int(input("Enter the second side:"))
c = int(input("Enter the third side:"))

if a+b>c and a+c>b and c+b>a:
    print("Yes, it is true that your measurements indicate a triangle")
else:
    print("No, according to the law of triangles, these dimensions connot represent a triangle")