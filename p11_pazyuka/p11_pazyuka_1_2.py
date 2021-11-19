# ВАШ КОД ТУТ
d = 0
def suml(lst):
    global d,i
    if d==0:
        i = len(lst)+1
        d = i
    i-=1
    if i==0:
      return 0
    else:
      return lst[i-1]+suml(lst)
def cons(head, tail=[]):
    return [head]+tail
# ПЕРЕВІРКА
l = cons(3, 
        cons(2, 
            cons(1, [])))
print(sum(l))
assert sum(l) == 6, 'Failed on sum'
print('All tests good!')
