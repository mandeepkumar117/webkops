text = input("Enter characters: ")

characters = []

for char in text:
    characters = characters + [char]

length = 0

for char in characters:
    length = length + 1

for i in range(length):
    for j in range(i + 1, length):
        if characters[i] > characters[j]:
            temp = characters[i]
            characters[i] = characters[j]
            characters[j] = temp

print(characters)