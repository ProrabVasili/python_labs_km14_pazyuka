# ВАШ КОД ТУТ
def akker(m,n):
  if m==0:
    return n+1
  elif n==0:
    return akker(m-1,1)
  else:
    return akker(m-1,akker(m,n-1))
# ПЕРЕВІРКА

test_pairs = list((m, n) for m in range(0,4) for n in range(0,5))
results = [
    1,  2,  3,  4, 5, 
    2,  3,  4,  5, 6, 
    3,  5,  7,  9, 11,
    5, 13, 29, 61, 125
]
for (m, n), res in zip(test_pairs, results):
    assert akker(m, n) == res, f'Failed test for (m, n) pair ({m}, {n}): akker({m}, {n}) = {res}'
print('All tests good!')
