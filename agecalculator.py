name=str(input("enter your name:"))
year=int(input("enter current year:"))
dob=int(input("enter your year of birth:"))
age=year-dob
if(age>=60):
    print(f"hello {name}, you are a senior citizen and your age is {age}")
else:
    print(f"hello {name}, you are not a senior citizen and your age is {age}")


    