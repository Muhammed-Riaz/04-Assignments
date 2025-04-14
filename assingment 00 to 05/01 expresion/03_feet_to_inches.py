# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.


def main():
    
    feet = int(input("Enter feet: "))
    inches = feet * 12
    print(f"{feet} feet is equal to {inches} inches.")

if __name__ == '__main__':
    main()