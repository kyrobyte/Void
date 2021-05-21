import random


def dice_roll():
    root = random.randint(1, 6)
    return root


player_1 = dice_roll()
player_2 = dice_roll()

for i in range(0, 10):
    print("Player 1 rolled", player_1)
    print("Player 2 rolled", player_2)
if player_1 > player_2:
    print("Player 1 won.")
if player_2 > player_1:
    print("Player 2 won.")
if player_1 == player_2:
    print("It is a tie.")
