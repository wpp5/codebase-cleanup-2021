from random import choice

def determine_winner(u,c):

    """
    Determines the winner of RPS, outputs winning choice, and prints a win, loss, or tie statement
    Param: both u and c will be string values either "rock","paper", or "scissors"

    Examples:
    determine_winner("rock","paper")
    determine_winner("rock","rock")
    """

    winning = {'paper':'scissors','rock':'paper','scissors':'rock'}

    if u == winning[c]:
        winner = u
        print("YOU WIN!")

    elif c == winning[u]:
        winner = c
        print("YOU LOSE!")

    else:
        winner = "tie"
        print("IT'S A TIE!")


    return winner 

if __name__ == '__main__':
        
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

    winner = determine_winner(u,c)
