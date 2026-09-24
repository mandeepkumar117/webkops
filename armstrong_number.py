num=int(input("Enter any number: "))
sum=0
length=0
temp=num
while num>0:
    num=num//10
    length +=1
num=temp
while num>0:
    last=num%10
    sum=sum+(last ** length)
    num=num//10
if temp == sum:
    print("number is armstrong number")
else:
    print("number is not armstrong number")
