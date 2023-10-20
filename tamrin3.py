N = input("Enter your first name:")
F = input("Enter you last name:")
a = int(input("Enter your physiology score:"))
b = int(input("Enter your pathology score:"))
c = int(input("Enter your biomechanics score:"))
MO = (a + b + c)/3
print(MO)
if MO>=17:
    print(N,F,"you Great")
if MO<17 and MO>=12:
    print(N,F,"you Normal")
if MO<12:
    print(N,F,"you Fail") 