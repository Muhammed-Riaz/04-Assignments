# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

# Here's a sample run (user input is in blue):

# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']
# Starter Code

def get_list():
    lst = []
    elem = input("Enter a value if value is done press enter :")
    while elem != "":
       lst.append(elem)
       elem = input("Enter a value if value is done press enter :")

    return lst   

def main():
    print(get_list())
if __name__ == '__main__':
    main()