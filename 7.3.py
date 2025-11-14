###
# A program that checks whether the number entered
# from the keyboard is even.
# A number is even if the remainder when divided by 2 is 0.
# What operator do you need to use to calculate
# the remainder of division?
#Postanowiłem zmienić program tak żeby pokazywał czy liczba jest parzysta czy niepatrzysta

number = int(input('Enter number: '))
calc = number % 2
ods = calc
if ods == 0:
    ex = 'even'
else:
    ex = 'odd'

print(f'Number is {ex}')