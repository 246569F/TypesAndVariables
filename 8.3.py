###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#
C = int(input('Input your room temperature in Celsius: '))
F = C * 1.8 +32
K = C + 273.15
print(f'The room temperature = {round(F, 2)} Fahrenheit or {K} Kelvin ')