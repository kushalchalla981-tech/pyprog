import math
n=int(input(f"enter element:"))
num=[]
for i in range(n):
    value=float(input(f"enter element {i+1}"))
    num.append(value)
mean=sum(num)/n
variance=sum((x-mean)**2 for x in num)/n
std_dev=math.sqrt(variance)
print(f"mean:{mean}")
print(f"variance:{variance}")
print(f"standard deviation:{std_dev}")