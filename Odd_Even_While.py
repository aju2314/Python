a=int(input("enter the first number"))
b=int(input("enter the second number"))
while a<=b:
    if a%2!=0:
        print("odd",a)
    elif a%2==0:
        print("even",a)
    a+=1
