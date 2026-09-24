num=int(input("Enter any number: "))
count=0
while num>0:
    last=num%10
    num=num//10
    count=count+1
print("total number is: ",count)