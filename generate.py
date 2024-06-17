import random
#this is importing everything from the random module. May be better if we want to create our own variable called choice. 
coin = random.choice(["heads", "tails"])
print(coin)


# this is only importing choice from the random module. Could be nicer than writing random.choice everywhere in the program. So it's up to preference.
from random import choice
coin = choice(["heads", "tails"])
print(coin)


number = random.randint(1, 10)
print(number)

cards = ["jack", "queen", "king", "ace", "joker"]
random.shuffle(cards)
for card in cards:
    print(card)