# mystr=input("Enter any string: ")
# reverse=""
# for char in mystr:
#     reverse=char+reverse
# if reverse==mystr:
#     print("given string is palindrom")
# else:
#     print("not palindrom")

# for palindrome number

num = int(input("Enter any number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if reverse == original:
    print("Given number is palindrome")
else:
    print("Not palindrome")
