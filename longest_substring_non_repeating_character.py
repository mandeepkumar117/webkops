text = input("Enter string: ")

longest = ""

for i in range(len(text)):
    current = ""

    for j in range(i, len(text)):
        if text[j] in current:
            break

        current = current + text[j]

        if len(current) > len(longest):
            longest = current

print("Longest substring:", longest)
print("Length:", len(longest))