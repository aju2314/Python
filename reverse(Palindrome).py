a=int(input("enter a number"))
original_number=a
reverse=0
while a>0:
    remainder= a%10
    reverse=(reverse*10)+remainder
    a = a // 10
print(reverse)
if reverse==original_number:
    print("It is a palindrome")
else:
    print("Normal number")

