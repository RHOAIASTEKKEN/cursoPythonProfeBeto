import random

cards = ["Diamons", "Spades", "Hearts", "Clubs"]
ranks = [1,2,3,4,5,6,7,8,9,10, "Jacks", "Queen", "King", "Ace"]


def pickCard():
    card = random.choice(cards)
    rank = random.choice(ranks)
    return(f"The {rank} of {card}")

print("Carta seleccionada es:\n", pickCard())