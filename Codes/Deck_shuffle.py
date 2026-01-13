import random
#creating ranks and suits
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
#creating full ordered deck
deck = [rank + " of " + suit for suit in suits for rank in ranks]
#printing original deck
print(f"Original deck:\n{deck}")
#printing shuffled deck
random.shuffle(deck)
print(f"Shuffled deck:\n{deck}")

