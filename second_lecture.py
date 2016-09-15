from string import punctuation

my_sentence = open("sample.txt")

my_counter_dictionary = {}

for letter in my_sentence:
    if letter in my_counter_dictionary.keys():
        my_counter_dictionary[letter] += 1
    else:
        my_counter_dictionary[letter] = 1

print(sorted(my_counter_dictionary.items(), key=lambda x: x[1]))


for word in open_file:
    if word in contents.keys():


print(sorted(my_counter_dictionary.items(), key=lambda x: x[1]))
