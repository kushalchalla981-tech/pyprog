my_list = [1, 2, 3, 4]

while True:
    print("\nlist operations")
    print("1. insertion")
    print("2. deletion")
    print("3. appending")
    print("4. display list")
    print("5. pop")
    print("6. clear list")
    print("7. exit")

    try:
        choice = int(input("enter your choice: "))
    except ValueError:
        print("invalid input, please enter a number")
        continue

    if choice == 1:
        element = int(input("enter element to insert: "))
        position = int(input("enter position to insert: "))
        my_list.insert(position, element)
        print("element inserted successfully")
    elif choice == 2:
        element = int(input("enter element to delete: "))
        if element in my_list:
            my_list.remove(element)
            print("element deleted successfully")
        else:   
            print("element not found in the list")
    elif choice == 3:
        element = int(input("enter element to append: "))
        my_list.append(element)
        print("element appended successfully")
    elif choice == 4:
        print("current list:", my_list)
    elif choice == 5:
        if my_list:
            popped_element = my_list.pop()
            print(f"popped element: {popped_element}")
        else:
            print("list is empty, cannot pop")
    elif choice == 6:
        my_list.clear()
        print("list cleared successfully")
    elif choice == 7:
        print("exiting the program")
        break
    else:
        print("invalid choice, please try again")