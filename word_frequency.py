# text = input("Enter any sentence: ")

# words = text.split()
# frequency = {}

# for word in words:

#     if word in frequency:
#         frequency[word] = frequency[word] + 1
#     else:
#         frequency[word] = 1

# print(frequency)

# without bulitin method

text = input("Enter any sentence: ")

words = []
word = ""

for char in text:

    if char != " ":
        word = word + char

    else:
        if word != "":
            words.append(word)
            word = ""

if word != "":
    words.append(word)

frequency = {}

for word in words:

    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1

print(frequency)