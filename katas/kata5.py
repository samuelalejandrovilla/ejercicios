tierra = 149597870
jupiter= 778547200
print (tierra)
print(jupiter)
distacia = tierra-jupiter
distacia_millas = distacia * 0.621
print (abs(distacia_millas))

distacia1 = float(input('distacia del planeta 1 al sol: '))
distacia2 = float(input('distacia del planeta 1 al sol: '))
distacia= distacia1-distacia2
distacia= abs(distacia)
distacia_millas= distacia * 0.621
print(f'la distacia en millas es: {abs(distacia_millas)}')