def reverse_capitals(word):
    word = list(word)

    for i in range(len(word)):
        if word[i].isupper():
            word[i] = word[i].lower()
        else:
            word[i] = word[i].upper()

    return ''.join(word)

print(reverse_capitals('abCdef'))