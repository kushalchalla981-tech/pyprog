numbers = [10, 20, 30, 20, 40, 10, 50, 30]
unique_list = []
for item in numbers:
    if item not in unique_list:
        unique_list.append(item)
print("Original List:", numbers)
print("List after removing duplicates:", unique_list)