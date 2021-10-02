#Блок введення інформації
speed = float(input('Input wind speed(km/h): '))
pd = 'Potential damage:'
#Блок виведення інформації
if speed<0:
    print('The wind speed can\'t be negative')
elif speed<=137:
    print(f'{pd} Minor')
elif speed<=177:
    print(f'{pd} Moderate')
elif speed<=217:
    print(f'{pd} Considerable')
elif speed<=266:
    print(f'{pd} Severe')
elif speed<=322:
    print(f'{pd} Devasting')
else:
    print(f'{pd} Incredible')
