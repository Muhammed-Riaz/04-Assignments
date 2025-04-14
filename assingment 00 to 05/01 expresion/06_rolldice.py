# Simulate rolling two dice, and prints results of each roll as well as the total.
# Starter Code

import random 
def main():
    die = random.randint(1,6)
    die2 = random.randint(1,6)
    total = die + die2
    print(f"Die 1 rolled: {die}")
    print(f"Die 2 rolled: {die2}")
    print(f"Total: {total}") 

if __name__ == '__main__':
    main()