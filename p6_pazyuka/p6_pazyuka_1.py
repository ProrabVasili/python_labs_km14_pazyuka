w = ['першу', 'другу']
a,b = [set(i.lower() for i in input(f'Введіть {w[i]} фразу: ') if i.isalpha()) for i in range(2)]
print(f'{"Можливо" if b.issubset(a) else "Неможливо"} скласти другу фразу з літер першої')
