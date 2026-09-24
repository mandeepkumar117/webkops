numbers=eval(input("enter list item: "))
length=0
for num in numbers:
    length=length+1
for i in range(length):
    for j in range(i+1,length):
        if numbers[i]<numbers[j]:
            temp=numbers[i]
            numbers[i]=numbers[j]
            numbers[j]=temp
print(numbers)