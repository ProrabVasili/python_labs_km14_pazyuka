a,num,k,n16 = ['перше','друге','третє', 'Ви ввели некоректні дані! Спробуйте знову :)'],[],0,[]
while k!=3:
  try:
    vv = int(input(f'Введіть {a[k]} число:  '))
  except:
    print(f'{a[3]}')
    continue
  if vv not in range(256):
    print(f'{a[3]}')
    continue
  num+=[vv]
  k+=1
for i in range(3):
    n,a = [],num[i]
    if a<16:
        n+=[f'0{a}']
    else:
        while a>=1:
            n+=[a%16]
            a//=16
    n16+=[n]
n16 = [i[::-1] for i in n16]
n16 = [chr(65+j%10) if int(j)>9 else j for i in n16 for j in i]
print(''.join(map(str,n16)))
