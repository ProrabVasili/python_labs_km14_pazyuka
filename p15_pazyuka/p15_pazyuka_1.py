from math import factorial as fact
"""
без рекурсії
"""
def newton(n):
    for j in range(n+1):
        yield [int(fact(j)/(fact(i)*fact(j-i))) for i in range(j+1)]
        
"""
рекурсія з акумулятором
"""
def newton2(n,k=0):
        if n+1!=k:
          yield [int(fact(k)/(fact(i)*fact(k-i))) for i in range(k+1)]
          yield from newton2(n,k+1)
          
"""
#рекурсія без акумулятора   
"""     
def newton3(n):
  if n!=-1:
      yield [int(fact(n)/(fact(i)*fact(n-i))) for i in range(n+1)]
      yield from newton3(n-1)
       
while True:
    try:
        n = input('Entered a integer positive number or 0: ')
        if n.isdigit() == False:
            raise Exception('You entered no integer positive number or 0')   
        break
    except Exception as exc:
        print(exc)
        
[print(*i) for i in newton(int(n))]
print()
[print(*i) for i in newton2(int(n))]
print()
[print(*i) for i in reversed(list(newton3(int(n))))]    
