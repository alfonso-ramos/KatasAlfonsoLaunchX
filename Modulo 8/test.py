# Planets and moons

from functools import total_ordering


planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

moons = planet_moons.values()

planets = len(planet_moons.keys())

total_moons = 0

for moon in moons:
    total_moons += moon

promedio = total_moons / planets
print(promedio)