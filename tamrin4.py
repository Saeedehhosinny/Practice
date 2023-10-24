import math

op = input("Enter op(sin, cos, tan, cot, factorial, sqrt)")
if op == "sin" or "cos" or "tan" or "cot" or "factorial" or "sqrt":
    c = float(input("Enter your number:"))
    pi = math.pi
    if op == " sin":
        z=(c*pi)/180 
        sin = math.sin(z)
    if op == "cos":
        z = (c*pi)/180
        cos = math.cos(z)
    if op == "tan":
        z = (c*pi)/180
    tan = math.tan(z)
    if op == "cot":
        z =float(input("Enter tan:"))
        cot = tan/1
    if op == "factorial":
        if c<0:
            print("Run agin")
        else:
            factorial = math. factorial(c)
    if op == "sqrt":
        if c<0:
            print("Run agin")
        else:
            sqrt = math. sqrt(c)
    print(z or c)