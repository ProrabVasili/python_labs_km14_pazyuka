suits = ['diamonds', 'clubs', 'hearts', 'spades']
s13 = ['A']+list(range(2,11))+['J','Q','K']
s52 = iter([f'{j} {i}' for i in suits for j in s13])
[print(next(s52)) for _ in range(53)]
