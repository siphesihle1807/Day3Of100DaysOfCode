print('''
*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Jumanji.")
print("Your mission is to find the treasure.") 
direction = input("Where would you like to go? Left or right? ")
if direction.lower() == 'left':
    print("Oops, you fell off a cliff. Game over.")
else:
    print("Lucky move! Your journey continues!")
    print("You are now facing a dilemma.")
    print("You are at the river bank.")
    move = input("What would you like to do? Swim or wait? ")
    if move.lower() == 'swim':
        print("Ooops, you forgot about the crocodile! Game over!")
    else:
        print("Wise choice! A boat came to the rescue")
        print("You have reached a cave.\nAnd to access what is beyond it you have to answer a riddle!")
        print("Here is your ridde.\nRemember you get only one try!")
        riddle_ans = input("What can children make but not see? ")
        if riddle_ans.lower() != 'noise':
            print("You have come far, but unfortunately your answer is incorrect. Goodbye!")
        else:
            print("You have answered successfully, and reached the treasure. Congratulations!")



