mystr=input("Enter a string: ")
dict1={}
for i in mystr:
    if i in dict1:#yadi hai
        dict1[i]=dict1[i]+1 # to count badha do
    else:
        dict1[i]=1
print(dict1)


# text = input("Enter any string: ")

# checked = ""

# for char in text:
#     if char not in checked:
#         print(char, ":", text.count(char))
#         checked = checked + char