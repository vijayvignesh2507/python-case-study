import random

def roll_dice():
    min_value = 1
    max_value = 6

    while True:
        dice_roll = random.randint(min_value, max_value)
        print("You rolled:", dice_roll)

        roll_again = input("Do you want to roll the dice again? (yes/no): ")
        if roll_again.lower() != "yes" and roll_again.lower() != "y":
            break

roll_dice()
