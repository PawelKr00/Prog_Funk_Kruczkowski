def capitalize_all_words(sentence):
    words = sentence.split()
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    return " ".join(words)

print(capitalize_all_words("ala ma kota i nie wie co z nim zrobić"))