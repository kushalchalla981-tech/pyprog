def count_case(text):
    upper = 0
    lower = 0
    for ch in text:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
    print("Number of Uppercase Letters:", upper)
    print("Number of Lowercase Letters:", lower)

string = input("Enter a string: ")
count_case(string)