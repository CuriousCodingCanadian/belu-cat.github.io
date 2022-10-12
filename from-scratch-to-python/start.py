foo = 10 #Equivilent scratch code:set [foo] to (10)
bar = "some text" #Equivilent scratch code:set [bar] to (some text)

foo += 1 #Equivilent scratch code:change [foo] by (1)

print("Hello World") #Equivilent scratch code:say (Hello World)
print(foo) #Equivilent scratch code:say [foo]

while not foo > 10: #Equivilent scratch code:repeat until [foo] > 10
    print(foo)
    
    while True: #Equivilent scratch code:say [foo]
        foo += 1

if foo > 10:
    print("foo is greater than 10")
elif foo < 10:
    print("foo is less than 10")
else
    print("foo is equal to 10")

if bar == "some text":
    print("bar is some text")

hand = ["ace","king","queen","jack","ten"] #Equivilent to defining a list called "hand" in scratch
hand.append("nine") #Equivilent scratch code:add (nine) to [hand]
hand.pop(0) #Equivilent scratch code:delete item (0) from list [hand]

from random import randint
foo = randint(1,10) #Equivilent scratch code:set [foo] to (pick random (1) to (10))

from random import choice
card = choice(hand) #Equivilent scratch code:set [card] to (item (random) of choice)

foo = "hello" + "world" #Equivilent scratch code:set [foo] to (join (hello) and (world))
card = hand[0] #Equivilent scratch code:set [card] to (item (1) of hand)
letter = card[0] #Equivilent scratch code:set [letter] to (letter (1) of [card])

card = input("What do you want card to be?") #Equivilent scratch code:ask (What do you want card to be?) | set [card] to (answer)
