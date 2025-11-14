###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('a=')
a = int(a)
b = input('b=')
b = int(b)
c = input('c=')
c = int(c)
print(f'The volume of a cuboid with sides {a}, {b} and {c} is {a*b*c} and his surface area is {a*b*2+a*c*2+b*c*2} ')
