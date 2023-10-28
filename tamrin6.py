import random

pc_number = random.randint(0,100)
guss=0
while True:
    user_number =int(input("Enter num:"))
    guss+=1

    if user_number == pc_number:
        print("ok!!")
        break
    if user_number < pc_number:
        print("Adad bozorg vared kon!!")
    if user_number > pc_number:
        print("Adad kochektar vared kon!!")
print(pc_number)
print("Number of guesses=" , guss)
