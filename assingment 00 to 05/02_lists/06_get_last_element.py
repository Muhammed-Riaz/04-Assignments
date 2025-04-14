# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.
# Starter Code


def get_last_element(lst):
    
    print(lst[-1])


def get_lst():

  lst = []

  elem = input("Please enter an element of the list or press only enter to stop :")

  while elem != "":
     lst.append(elem)
     elem = input("Please enter an element of the list or press enter to stop: ")
  return lst

def main():
 lst = get_lst()
 get_last_element(lst)
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
  main()