def check_anagrams(word1, word2):
    if list(word1) == list(reversed(list(word2))):
        return True
    return False

print(check_anagrams("abcdef", "fedcba"))
print(check_anagrams("adsjkh", 'kjvcsh'))