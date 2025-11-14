#program sprawdzający czy samochód może jechać po autostradzie w sposób prosty
speed = int(input('Enter vehicle speed: '))
fast = speed <= 140 and speed >= 40
print(f'Speed is valid: {bool(fast)}')
