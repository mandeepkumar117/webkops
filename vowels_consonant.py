# text = input("Enter any string: ")

# vowels = 0
# consonants = 0

# for char in text:

#     if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
#         vowels = vowels + 1

#     elif char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
#         vowels = vowels + 1

#     elif (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
#         consonants = consonants + 1

# print("Vowels:", vowels)
# print("Consonants:", consonants)



# check karna hai ki vowels hai ya consonant

char = input("Enter any character: ")

if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    print("Vowel")

elif char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
    print("Vowel")

elif (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
    print("Consonant")

else:
    print("Not an alphabet")