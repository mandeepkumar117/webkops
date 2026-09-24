number=eval(input("enter list item: "))
result=[]
for num in number:
    if num not in result:
        result=result+[num]
print(result)