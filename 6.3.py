###
# A program that prints a university abbreviation
#   
university = "Krakow University of Economics"
r = ''.join(word[0].upper() for word in university.split()) 
#powyżej próbuje użyć funkcji nalezionych w internecie ale nie udało mi się pozbyć "O"
print(university[0]+university[7]+university[21])
print(r)