
planets = ["0", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planet = input("Choose a planet from the solar sytem to know your weight on that planet ")
weight = input("Now give your weight(kg) ")
weight = int(weight)
planet_2 = planets.index(planet)



# Write an if statement below:
if planet_2 == 1:
  weight = weight * 0.38
elif planet_2 == 2:
  weight = weight * 0.91
elif planet_2 == 3:
  weight = weight * 1
elif planet_2 == 4:
  weight = weight * 0.38
elif planet_2 == 5:
  weight = weight * 2.34
elif planet_2 == 6:
  weight = weight * 1.06
elif planet_2 == 7:
  weight = weight * 0.92
elif planet_2 == 8:
  weight = weight * 1.19
print(f"Your weight on {planet} is {weight}")
