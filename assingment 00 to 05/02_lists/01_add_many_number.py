# Write a function that takes a list of numbers and returns the sum of those numbers.
# Starter Code

def main(num_list):
    total = 0
    for add in num_list:
        total += add
    return total      

if __name__ == '__main__':
    # Ask the user to input numbers separated by spaces
    user_input = input("Enter a list of numbers separated by spaces: ")
    # Convert input string into a list of integers
    get_list = [int(x) for x in user_input.split()]
    # Call the function and print result
    result = main(get_list)
    print(f"Sum is: {result}")
