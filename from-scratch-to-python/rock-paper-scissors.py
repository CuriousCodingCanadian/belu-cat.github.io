'''
This is rock paper scissors. if you didnt know that, get out

'''

from random import choice

def youchoose(q: bool):
    userin = 'Banana'
    while userin.title() not in ["Rock", "Paper", "Scissors", 'Q']:
        if userin.title() != 'Banana': print('Invalid input')
        if not q: userin = input("Please enter your choice: "); continue
        else: userin = input("Please enter your choice, or Q to quit: ")
    return userin.title() 

def computerchoose():
    return choice(["Rock", "Paper", "Scissors"])

def outputtie(choice):
    print(f'Tie :| You chose {choice} and the computer chose {choice}')

def outputloss(choice, cchoice):
    print(f'You lose :( You chose {choice} and the computer chose {cchoice}')

def outputwin(choice, cchoice):
    print(f'You win :) You chose {choice} and the computer chose {cchoice}')

def results(wins, ties, losses):
    print('|', '-'*(maxlen:=(8+(int(len(str(sorted([wins,ties,losses])[-1])))))), '|')
    print('| Wins: ', wins,' '*(maxlen-(6+(len(str(wins))))), ' |', sep='')
    print('| Losses: ', losses,' '*(maxlen-(8+len(str(losses)))), ' |',sep='')
    print('| Ties: ', losses,' '*(maxlen-(6+len(str(losses)))), ' |',sep='')
    print('|', '-'*((maxlen)), '|')
    
def main():
    rps = ["Rock", "Paper", "Scissors", "Rock"]
    rpsdict = {"Rock":"Paper", "Paper":"Scissors", "Scissors":"Rock"}
    wins = 0
    losses = 0
    ties = 0
    banana = 'banana'
    while True:
        choice = youchoose(banana != 'banana')
        cchoice = computerchoose()
        beatscchoice = rpsdict[cchoice]

        if choice == 'Q': break
        
        if choice == cchoice: outputtie(choice); ties += 1
        
        elif choice == beatscchoice: outputwin(choice, cchoice); wins += 1
            
        else: outputloss(choice, cchoice); losses += 1

        banana = 'apple'
    


    results(wins, ties, losses)
    #print("You lost " + str(losses) + " times.")
    #print("You won " + str(wins) + " times.")
    #print("It was a tie " + str(ties) + " times.")

if __name__ == '__main__':
    main()
