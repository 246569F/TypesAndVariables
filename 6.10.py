###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"
upper_movie = movie.upper()
lower_movie = movie.lower()
# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print(f'{upper_movie}')
# print title in small letters
print(f'{lower_movie}')

# print how many times the vowel "e" appears in the title
print(f'{movie.count('e')}')
# print where in the text is the word "Lord"
a = 'Lord'
#znajdujemy slowo 
pos = movie.find(a)
#jeżeli nie znalezione zwracamy
if pos == -1:
    res = 'Brak takiego słowa'
#jeżeli znalezione liczymy pozycje i dodajemy 1 żeby nie wyszło 0
else:
    res = movie[:pos].count(' ') + 1
print(res)
# print where in the text is the word "dragon"
b = 'dragon'
#Tak samo jak wcześniej 
pos = movie.find(b)
if pos == -1:
    res = 'Brak takiego słowa'
else:
    res = movie[:pos].count(' ') + 1
print(res)