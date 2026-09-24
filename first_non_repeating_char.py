text = input("Enter any string: ")

for i in range(len(text)):

    count = 0

    for j in range(len(text)):

        if text[i] == text[j]:
            count = count + 1

    if count == 1:
        print("First non-repeating character:", text[i])
        break