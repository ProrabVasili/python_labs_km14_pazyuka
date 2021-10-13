w = ['першу', 'другу']
a = [set(i.lower() for i in input(f'Введіть {w[i]} фразу: ') if i.isalpha()) for i in range(2)]
[print(f'Множина унікальних літер {w[i]} фрази: {a[i]}') for i in range(2)]
print(f'{"Можливо" if a[1].issubset(a[0]) else "Неможливо"} скласти другу фразу з літер першої')
