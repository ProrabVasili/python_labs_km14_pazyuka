#Блок введення інформації
age = int(input('Input age: '))
#Блок виведення інформації
print('The age can\'t be negative' if age<0 else f'{age} calendar year(-s) is {age*10.5 if age<=2 else 21+(age-2)*4} dog year(-s)') 

