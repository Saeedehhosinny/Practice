import random

n = int(input("How many numbers do you want?"))
l = []
for i in range(n):
    i= random.randint(1,1000)
    l.append(i)
print(l)