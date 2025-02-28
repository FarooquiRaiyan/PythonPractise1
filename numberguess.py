import random

comp_num= random.randint(1,100)
print(comp_num)

myinp=""
while myinp!= "Exit":
    myinp =input("enter the umber to be guess")
    if int(myinp) ==comp_num:
        print("you guess it write")
        exit()
    elif int(myinp) <comp_num:
        print("Too low")
    elif int(myinp)>comp_num:
        print("Too high")
    elif int(myinp)=="Exit":
        print("Exiting")