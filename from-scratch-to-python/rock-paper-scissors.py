from random import choice

def youchoose():
    userin = 'Banana'
    while userin.title() not in ["Rock", "Paper", "Scissors"]:
        if userin != 'Banana': print('Invalid Output')
        userin = input("Please enter your choice: ")
    return userin.title() 

def computerchoose():
    return random.choice(["Rock", "Paper", "Scissors"])

def outputtie(choice):
    print(f'Tie :| You chose {choice} and the computer chose {choice}')

def outputloss(choice, cchoice):
    print(f'You lose :( You chose {choice} and the computer chose {cchoice}')

def outputwin(choice, cchoice):
    print(f'You win :) You chose {choice} and the computer chose {cchoice}')
    
def main():
    rps = ["Rock", "Paper", "Scissors", "Rock"]
    wins = 0
    losses = 0
    ties = 0
    continue = True
    while continue:
        choice = youchoose()
        cchoice = computerchoose()
        beatschoice = rps[rps.index(choice)+1]
        if choice == cchoice:
            outputtie(choice)
            ties += 1
        
        if choice == beatscchoice:
            outputwin(choice, cchoice)
            wins += 1
            
        else: outputloss(choice, cchoice); losses += 1
    
    
        userin = 'Banana'
        while userin.title() not in ['True', 'False']:
            if userin != 'Banana': print('Invalid input')
                userin = input('Continue? (True/False)')
                if eval(userin): continue
                else: break
# not complete    


print("You lost " + str(losses) + " times.")
print("You won " + str(wins) + " times.")
print("It was a tie " + str(ties) + " times.")
