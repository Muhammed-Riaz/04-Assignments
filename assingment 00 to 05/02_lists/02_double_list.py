# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]
# Starter Code

def main(num_list):
    double = []
    for element in num_list:
        double.append(element+element)
    return double   
   
if __name__ == '__main__':
    get_list = input("Enter a list with seprate spaces :")
    user_list = [int(x) for x in get_list.split()]

    print(main(user_list))
