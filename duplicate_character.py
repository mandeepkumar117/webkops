text = input("Enter any string: ")
length = 0
for char in text:
    length = length + 1

for i in range(length):
    for j in range(i + 1, length):

        if text[i] == text[j]:
            print(text[i])
#             break

# using bulit in method

# text = input("Enter any string: ")

# for i in range(len(text)):
#     for j in range(i + 1, len(text)):

#         if text[i] == text[j]:
#             print(text[i])
#             break