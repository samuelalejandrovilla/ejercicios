planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets.append('Pluto')
print(f'el total de planetas es de : {len(planets)}, y el ultimo planeta es: {planets[-1]}')


planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

nombre=input['deme el nombre del planeta quiere buscar: ']
indice= planets.index(nombre)

print(planets[0:indice])

print(planets[indice+1:])