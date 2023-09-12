print("1.Add \n 2.Sub \n 3.Multi \n 4.Div")
c=int(input("enter the choice:"))
a=int(input("enter the number:"))
b=int(input("enter the number:"))
if c==1:
    result=a+b
    print(result)
elif c==2:
    result=a-b
    print(result)
elif c==3:
    result=a*b
    print(result)
elif c==4:
    result=a/b
    print(result)
else:
    print("enter proper operator")
