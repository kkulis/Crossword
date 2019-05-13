import random

width = 10
height = 10
words_min = 5
words_crosses = 2
board = []
dictionary = []


f = open("słowa.txt", "r")

for item in f:
    dictionary.append(item.rstrip())
dictionary.remove(dictionary[1])
f.close()

lst = ["."] * (height * width)
chars = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'

words = 0 
while words < words_min:
    if words % 2 == 0:
        word_number = random.randint(0, len(dictionary)) - 1
        word_place = random.randint(0,len(lst)) - 1
        word_len = len(dictionary[word_number])
        horizontal = word_place // width
        empty_horizontal = True
        j = 0
        try:
            empty_horizontal = all([lst[i] == '.' for i in range(word_place, word_place + word_len)])
        except Exception:
            empty_horizontal = False 
        if ((word_place + word_len) < ((horizontal + 1) * width)) and empty_horizontal == True:
            for i in range(word_place, word_place + word_len):
                lst[i] = dictionary[word_number][j]
                j += 1
            words += 1
        
    else:
        word_number = random.randint(0, len(dictionary)) - 1
        word_place = random.randint(0, len(lst)) - 1
        word_len = len(dictionary[word_number])
        empty_vertical = True
        j = 0 
        try:
            empty_vertical = all([lst[i] == '.' for i in range(word_place, word_place + width * word_len, width)])
        except Exception:
            empty_vertical = False
        if (word_place % width) == ((word_place + width * word_len) % width) and empty_vertical == True:
            for i in range(word_place, word_place + width * word_len, width):
                lst[i] = dictionary[word_number][j]
                j += 1
            words += 1
else:
    for i in range(len(lst)):
        if lst[i] == '.':
            lst[i] = chars[random.randint(0, len(chars)) - 1]
for i in range(0, (height * width), width):
    for j in range(width):
        print(lst[i+j], '|', end= '')
    print()
board = lst  

print(board)


