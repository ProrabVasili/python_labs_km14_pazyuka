words = []
while True:
    word = input('Enter a word: ')
    words += [word]
    vidp = input('Do you want to enter another word? (Press "Enter" if you want to continue)')
    if vidp != '':
        break
print(*words if len(words)<2 else (', '.join(words[:-1]), f'and {words[-1]}'))
