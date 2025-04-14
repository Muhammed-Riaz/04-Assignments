def main():
    # Step 1: Get user's Earth weight
    earth_weight = float(input("Enter a weight on Earth: "))

    # Step 2: Ask for planet name
    planet = input("Enter a planet: ")

    # Step 3: Planet gravity dictionary (as a multiplier of Earth weight)
    gravity_factors = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    # Step 4: Calculate and print the equivalent weight
    if planet in gravity_factors:
        planet_weight = earth_weight * gravity_factors[planet]
        print(f"The equivalent weight on {planet}: {round(planet_weight, 2)}")
    else:
        print("That planet is not in our solar system!")

# Run the program
main()


