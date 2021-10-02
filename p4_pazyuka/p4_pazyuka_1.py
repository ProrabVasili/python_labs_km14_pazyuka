a = ['name','surname','phone number','street','number of house','apartment number','city','zip code','country']
#Блок введення інформації
name, surname,pnumber, street, hnumber, anumber, city, zcode, country = [input(f'Input your {a[i]}: ') for i in range(9)]
#Блок виведення інформації
print(f'{name} {surname}',f'{pnumber}',f'Str.{street} {hnumber}, ap.{anumber}, {city}',f'{zcode}',f'{country}', sep='\n')
