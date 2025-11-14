###
# A program that prints your height both in cm and in feet and inches.
#chyba ładniej było by to zrobić round
cm = int(input("What's your height in cm: "))
feet = cm // 30.47999902
a = cm % 30.47999902
inches = a //2.54
# calculate the number of feet

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')