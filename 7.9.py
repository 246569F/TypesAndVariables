import random
dice_roll = random.randint(1,6)
special = dice_roll == 6 or dice_roll == 1
print(dice_roll)
print(bool(special))