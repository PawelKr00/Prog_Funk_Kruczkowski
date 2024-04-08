def filter_long_words(words):
    average = 0
    for word in words:
        average += len(word)
    average = average / len(words)
    output = []
    for word in words:
        if len(word) > average:
            output.append(word)
    return output

print(filter_long_words(['asda','asdasff','sdfdsfsdf','sddsf']))