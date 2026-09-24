str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) != len(str2):
    print("Not Anagram")
else:

    checked = ""
    is_anagram = True

    for char in str1:

        if char in checked:
            continue

        count1 = 0
        count2 = 0

        for x in str1:
            if x == char:
                count1 = count1 + 1

        for x in str2:
            if x == char:
                count2 = count2 + 1

        if count1 != count2:
            is_anagram = False
            break

        checked = checked + char

    if is_anagram:
        print("Anagram")
    else:
        print("Not Anagram")