
from random import choice

#
# USER SELECTION
#

VALID_OPTIONS = ["rock","paper","scissors"]
u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
print("USER CHOICE:", u)
if u not in VALID_OPTIONS:
    print("OOPS, TRY AGAIN")
    exit()

#
# COMPUTER SELECTION
#

c = choice(VALID_OPTIONS)
print("COMPUTER CHOICE:", c)

#
# DETERMINATION OF WINNER
#

if u== "rock":
    if c == "rock":
        print("It's a tie!")
    elif c == "paper":
        print("You lose!")
    elif c == "scissors":
        print("okay")

#There are even less ways either using a dictionary or tuple approqach 

winning = {'paper':'scissors','rock':'paper','scissors':'rock'}


if u == winning[c]:
    print("You win!",u,'beats',c)
elif c == winning[u]:
    print("You lose!",c,'beats',u)
else:
    print("You both chose",c,". It's a tie!")