import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []


def get_random_card():
    return random.choice(diamonds)


while diamonds:
    card = input("Press enter to pick a card:\n Type: Q to exit ")
    if card == "Q":
        break

    new_card = get_random_card()
    hand.append(new_card)
    diamonds.remove(new_card)

    print("Your hand: {}".format(hand))
    print("Cards Remaining: {}" .format(diamonds))

    if not diamonds:
        print("No cards left")
