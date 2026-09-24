mystr=input("Enter any string: ")
result=""
for char in mystr:
    if char not in result:
        result=result+char
print(result)