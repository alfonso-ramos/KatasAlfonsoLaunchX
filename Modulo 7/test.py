new_planet = ""

planets = []

while new_planet != "done":
    if new_planet:
        planets.append(new_planet)
    new_planet = input("Enter a new value, or 'done' when done ")

for planet in planets:
    print(planet)