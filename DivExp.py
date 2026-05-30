import sys
def DivExp(a,b):
    assert a>0
    try:
        c=a/b
    except ZeroDivisionError:
        print("value of b cannot be zero")
        sys.exit(0)
    else:
        return c
value1=int(input("enter value of a:"))
value2=int(input("enter value of b:"))
value3=DivExp(value1,value2)
print(value1, "/", value2, "=", value3)