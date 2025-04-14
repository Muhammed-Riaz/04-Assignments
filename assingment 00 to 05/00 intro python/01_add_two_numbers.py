# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

#     Prompt the user to enter the first number.

#     Read the input and convert it to an integer.

#     Prompt the user to enter the second number.

#     Read the input and convert it to an integer.

#     Calculate the sum of the two numbers.

#     Print the total sum with an appropriate message.

# The provided solution demonstrates a working implementation of this problem, where the main() function guides the user through the process of entering two numbers and displays their sum.


def main():
  user1 = input("Enter your 1st number :")
  interger = int(user1)
  user2 = input("Enter a second number : ")
  interger2 = int(user2)
  sum = interger + interger2
  print(sum)
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
 main()



