from random import choice

def youchoose():
    userin = 'Banana'
    while userin.title() not in ["Rock", "Paper", "Scissors"]:
        userin = input("Please enter your choice: ")
    return userin.title() 
    
opponentchose = "Your opponent chooses"

def opponentchoose():
    return random.choice(["Rock", "Paper", "Scissors"])

def main():
    rps = ["Rock", "Paper", "Scissors"]
    wins = 0
    losses = 0
    ties = 0
    choice = youchoose()
    uchoiceset = set()
    
    
# not complete    
    
    

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
