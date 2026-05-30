a=int(input("enter first number: "))
b=int(input("enter second number: "))
choice=int(input("enter your choice: 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: "))
if choice==1:
    print(f"the sum of {a} and {b} is: {a+b}")
elif choice==2:
    print(f"the difference of {a} and {b} is: {a-b}")
elif choice==3:
    print(f"the product of {a} and {b} is: {a*b}")
elif choice==4:
    if b!=0:
        print(f"the quotient of {a} and {b} is: {a/b}")
    else:
        print("division by zero is not allowed")
else:
    print("invalid choice")
