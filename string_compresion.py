text = input("Enter any string: ")

result = ""
count = 1

for i in range(len(text) - 1):

    if text[i] == text[i + 1]:
        count = count + 1

    else:
        result = result + text[i] + str(count)
        count = 1

result = result + text[-1] + str(count)

print("Compressed string:", result)