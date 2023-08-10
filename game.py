import random
# snake water gun 
def gameWin(comp, you):
    # if two values are equal declare a tie !
    if comp == you:
        return None

    # check for all possibilities when computer choose s
    elif comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True

    # check for all possibilities when computer choose w
    elif comp == "w":
        if you == "g":
            return False
        elif you == "s":
            return True

    # check for all possibilities when computer choose g
    elif comp == "g":
        if you == "s":
            return False
        elif you == "w":
            return True

print(" Computer Turn : Snake(s) Water(w) Gun(g)?")
randNo = random.randint(1, 3)

if randNo == 1:
    comp = "s"
elif randNo == 2:
    comp = "w"
elif randNo == 3:
    comp = "g"

you = input(" Your's Turn : Snake(s) Water(w) Gun(g)?")

a = gameWin(comp, you)

print(f"Computer choose {comp}")
print(f"You choose {you}")

if a == None:
    print("The game is a tie !!! ")
elif a:
    print("You Win !!!")
else:
    print("You Loose !!! ")
