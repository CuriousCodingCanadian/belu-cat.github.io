from random import randint

def youchoose():
    youchoseappend = "You choose"
    if choice == "rock":
        print(youchoseappend + " Rock")
    elif choice == "paper":
        print(youchoseappend + " Paper")
    elif choice == "scissors":
        print(youchoseappend + " scissors")

randchoice = randint(1,3)
def randchoose():
    youchoseappend = "Your opponent chooses"
    if randchoice == 1:
        print(youchoseappend + " Rock")
    elif randchoice == 2:
        print(youchoseappend + " Paper")
    elif randchoice == 3:
        print(youchoseappend + " scissors")

def check():
    wins = 0
    losses = 0
    ties = 0
    if choice == "paper":
        if randchoice == 1:
            print("You won!")
            wins += 1
    
        if randchoice == 2:
            print("It was a tie.")
            ties += 1
    
        if randchoice == 3:
            print("Your opponent won.")
            losses += 1

    if choice == "rock":
        if randchoice == 1:
            print("It was a tie.")
            ties += 1
    
        if randchoice == 2:
            print("Your opponent won.")
            losses += 1
    
        if randchoice == 3:
            print("You won!")
            wins += 1

    if choice == "scissors":
        if randchoice == 1:
            print("Your opponent won.")
            losses += 1
    
        if randchoice == 2:
            print("You won!")
            wins += 1
    
        if randchoice == 3:
            print("It was a tie.")
            ties += 1

x = 0
while x < 10:
    choice = input("What do you want to play")
    youchoose()
    randchoose()
    check()
    x += 1

# print("You lost " + str(losses) + " times.")
# print("You won " + str(wins) + " times.")
# print("It was a tie " + str(ties) + " times.")