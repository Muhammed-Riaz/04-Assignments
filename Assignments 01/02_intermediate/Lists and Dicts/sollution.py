def access_element(lst, index):
    if 0 <= index < len(lst):
        return f"Element at index {index}: {lst[index]}"
    else:
        return "Index out of range."

def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        old = lst[index]
        lst[index] = new_value
        return f"Replaced '{old}' with '{new_value}' at index {index}."
    else:
        return "Index out of range."

def slice_list(lst, start, end):
    if start < 0 or end > len(lst) or start > end:
        return "Invalid slice indices."
    return f"Sliced list: {lst[start:end]}"

def print_list(lst):
    print("Current List:", lst)

def index_game():
    my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    print("🎮 Welcome to the Index Game!")
    
    while True:
        print_list(my_list)
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == '1':
            try:
                idx = int(input("Enter the index to access: "))
                print(access_element(my_list, idx))
            except ValueError:
                print("Please enter a valid integer index.")

        elif choice == '2':
            try:
                idx = int(input("Enter the index to modify: "))
                new_val = input("Enter the new value: ")
                print(modify_element(my_list, idx, new_val))
            except ValueError:
                print("Invalid input.")

        elif choice == '3':
            try:
                start = int(input("Enter start index: "))
                end = int(input("Enter end index: "))
                print(slice_list(my_list, start, end))
            except ValueError:
                print("Invalid input.")

        elif choice == '4':
            print("Thanks for playing! 👋")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

        print("\n" + "-"*40)

# Run the game
index_game()
