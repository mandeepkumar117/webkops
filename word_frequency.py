text = input("Enter any sentence: ")   # User se sentence lena

words = []                            # Saare words ko store karne ke liye empty list
word = ""                             # Ek-ek word banane ke liye empty string

for char in text:                     # Sentence ke har character ko ek-ek karke lena

    if char != " ":                   # Agar character SPACE nahi hai
        word = word + char            # Character ko current word mein add karo

    else:                             # Agar SPACE mil gaya

        if word != "":                # Agar word empty nahi hai
            words.append(word)        # Word ko words list mein add karo
            word = ""                 # Word ko empty karo, next word ke liye


if word != "":                        # Sentence ke end mein agar koi word bacha hai
    words.append(word)                # Us last word ko list mein add karo


frequency = {}                        # Word frequency store karne ke liye dictionary

for word in words:                    # Words list ke har word ko ek-ek karke lena

    if word in frequency:             # Agar word dictionary mein already hai
        frequency[word] = frequency[word] + 1  # Uski frequency 1 se badhao

    else:                             # Agar word dictionary mein nahi hai
        frequency[word] = 1           # Pehli baar hai, isliye frequency 1


print(frequency)                      # Final word frequency print karo