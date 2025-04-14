# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

import random


def main():
     for i in range(3):
        die1 = random.randint(1, 6)  # local
        die2 = random.randint(1, 6)  # local
        total = die1 + die2
        print("Roll", i+1, "→ Die 1:", die1, "Die 2:", die2, "| Total:", total)

if __name__ == '__main__':
   main()