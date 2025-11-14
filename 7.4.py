#program do sprawdzania czy drzewo można ściąć 
import math
tree = int(input('Tree circumference in cm: '))
r = tree / math.pi
pos = r
if pos <= 50:
    ex = 'Cuting this tree is prohibited'
else:
    ex = 'You have permission to cut down this tree '
print(ex)