import random

while True:
    a = input("Do you want play or quit?")
    if a == "quit":
        break
    if a == "play":
        d = random. randint(1,6)
        if d == 6:
            d = random.randint(1,6)
            print("you have a prize")
    
        