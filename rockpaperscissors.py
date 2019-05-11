'''Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them,
print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock'''

def game(a,b):
    if a == b:
        print "draw"
    else:
        if a == "R" and b == "S":
            print "player 1 won, congratulations"
        elif b == "R" and a == "S":
            print "player 2 won, congratulations"
        elif a == "S" and b == "P":
            print "Player 1 won, congratulations"
        elif b == "S" and a == "P":
            print "Player 2 won, congratulations"
        elif a == "P" and b == "R":
            print "player 1 won, congratulations"
        elif b == "P" and a == "R":
            print "player 2 won, congratulations"
        else:
            print "INVALID INPUT"

while True:
    x = raw_input("Would you like to start a new game? (Y/N)" )
    if x == "Y":
        a = raw_input("Player 1: R,P,S? ")
        b = raw_input("Player 2: R,P,S? ")
        game(a,b)
    else:
        print ("Thanks, next time")
        break
