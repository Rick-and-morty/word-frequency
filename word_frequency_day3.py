
from string import punctuation
# my first try, didnt want to make it worse so i started over

with open("sample.txt") as open_file:
    contents = open_file.read()
    contents = contents.lower()
    for item in punctuation:
        contents = contents.replace(item, "")
    contents = contents.replace("\n", " ")
    book = contents.split(" ")
    word_count = {}
    for gamma in book:
        if gamma in word_count.keys():
            word_count[gamma] += 1
        else:
            word_count[gamma] = 1
    word_count = (sorted(word_count.items(), key=lambda x: x[1]))
    word_count = word_count[-21: -1]
    for group in reversed(word_count):
        print(*group)
