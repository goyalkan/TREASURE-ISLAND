print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


direction = input("where you want to go? , left or right\n ")

if direction == "right":
    print("fall into a hole , GAME OVER")
elif direction == "left" :
    choose = input("you want to swim or wait?, swim or wait \n")
    if choose == "swim":
        print("attacked by trout , GAME OVER")
    elif choose == "wait":
        door = input("which door, red, blue,yellow\n")
        if door == "red":
            print("burned by fire , GAME OVER")
        elif door == "blue":
            print("eaten by beasts, GAME OVER")
        elif door == "yellow":
            print("YOU WIN!")
        else :
            print("GAME OVER :(")   
    else :
        print("attacked by trout, GAME OVER")  

else :
    print("fall into a hole, GAME OVER")    








