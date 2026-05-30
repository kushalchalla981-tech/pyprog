from math import sqrt
num=(input("enter number:"))
print(f"the entered number is: {num}")
uniqDig=set(num)
for element in uniqDig:
    print(f"{element} occurs {num.count(element)} times")