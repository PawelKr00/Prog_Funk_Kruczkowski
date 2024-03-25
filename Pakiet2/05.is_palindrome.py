def is_palinrome(word):
    return word.lower().replace(' ', '') == word[::-1].lower().replace(' ', '')

print(is_palinrome('kajA    k'))
print(is_palinrome('kadsjA    k'))
print(is_palinrome('kk   ka jA    kkk'))