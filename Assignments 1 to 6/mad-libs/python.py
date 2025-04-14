def mad_libs():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")
    food = input("Enter your favorite food: ")
    superpower = input("Enter a superpower: ")
    friend = input("Enter a friend's name: ")

    story = f"""
    Once upon a time in {place}, there lived a {age}-year-old adventurer named {name}.
    One day, while exploring the mysterious caves of {place}, {name} stumbled upon a hidden door.
    As soon as {name} opened the door, a {animal} appeared and spoke in a deep voice,
    "Only those who love {food} can pass!" 

    Without hesitation, {name} took out a plate of {food} and offered it to the {animal}.
    The creature smiled and granted {name} an incredible superpower: {superpower}!
    Now, with the help of {friend}, {name} sets out on a thrilling journey to save the world.

    And so, the legend of {name}, the {superpower}-powered hero of {place}, began...
    """

    print(story)

mad_libs()















  # story = (f"Once upon a time, there was a {adjective1} {noun1} who loved to {verb1} {adverb1}. "
  #          f"One day, it met a {adjective2} {noun2} who could {verb2} {adverb2}. "
  #          f"Together, they became the best of friends and had many adventures.")