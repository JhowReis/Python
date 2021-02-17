# Look for the treasure ... good luck and don't forget that this can be dangerous


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
left_right = str(input("You're across road.\nWhere do you want to go. Left or Right [L/R]")).upper()
if left_right == "R":
    print("Fall into a hole Game Over")
else:
    swim_wait = str(input('You come to a lake, There is an island in the middle of lake \ntype "wait" to wait a boat. type "swim" to swim across')).upper()
    if swim_wait == "SWIM":
        print("Attacked by trout. Gamer over")
    else:
        choice_door = str(input("You arrive at the island unharmed.\nThere is  3 doors. One red, yellow and one blue. Wich color do you choice")).upper()
        if choice_door == "RED":
            print("Burned by fire.Game Over")
        elif choice_door == "BLUE":
            print("Eaten by beasts. Game Over")
        elif choice_door == "":
            print("Game Over")
        else:
            print("Congratulations. You win!")


#@JonathanReis
#jonathan.linkedin2019@gmail.com