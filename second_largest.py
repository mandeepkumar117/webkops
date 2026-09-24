numbers=eval(input("Enter any array number: "))
if numbers[0] > numbers[1]:
    high=numbers[0]
    shigh=numbers[1]
else:
    high=numbers[1]
    shigh=numbers[0]
for i in range(2,len(numbers)):
    if numbers[i]>high:
        shigh=high
        high=numbers[i]
    else:
        shigh=numbers[i]
print("second highest element: ",shigh)