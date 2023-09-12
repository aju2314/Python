print("90 and above:S \n 85 and above:A+ \n 80 and above:A \n 75 and above:B+ \n 70 and above:B \n 65 and above:C+ \n 60 and above:C \n 5o and above:D \n below 50:F")
a=int(input("Enter a value"))
if a>=90:
    print("Grade is S")
elif a>=85:
    print("Grade is A+")
elif a>=80:
    print("Grade is A")
elif a>=75:
    print("Grade is B+")
elif a>=70:
    print("Grade is B")
elif a>=65:
    print("Grade is C+")
elif a>=60:
    print("Grade is C")
elif a>=50:
    print("Grade is D")
else:
    print("FAIL")
