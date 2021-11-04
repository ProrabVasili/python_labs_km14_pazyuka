from itertools import permutations
from functools import reduce
import numpy as np

#дана функція призначена для створення квадратної матриці з випадкових чисел розмірністю nxn
def random_matrix(n):
    matrix = np.random.randint(10, size = (n, n))
    return matrix

#дана функція призначена для створення списку (perestanovka) усіх перестановок чисел від 1 до n
def permutation(n):
    perestanovka = list(permutations(''.join(map(str,range(1,n+1))), n))
    return perestanovka

#дана функція призначена для створення списку (mult) добутків з урахуванням кількості інверсій, що характеризує "+" чи "-"
def multiply(lst):
    ch = [[matrix[int(j)][int(i[j])-1] for j in range(n)] for i in lst]
    pon = [len([1 for j in range(len(i)-1) for k in range(j+1,len(i)) if int(i[j])>int(i[k])]) for i in lst]
    mult = [(-1)**pon[i]*reduce(lambda x,y: x*y,ch[i],1) for i in range(len(ch))]
    return mult

#дана функція створена для підрахунку суми добутків
def add(mlst):
    return sum(mlst)


n=input('Введіть розмірність квадратної матриці одним числом n (nєN):')
try:
    if len(n.split())==0:
        raise Exception('Пусто :(')
    elif all(map(lambda x: x.isdigit(),n.split()))==False:
        raise Exception('У введенні знаходяться інші символи!')
    elif len(n.split())>1:
        raise Exception(f'Ви ввели не 1 натуральне число, а {len(n.split())}')
    n = int(n)
    matrix = random_matrix(n)
    print(f'Визначник (за власними функціями): {add(multiply(permutation(n)))}')
    print(f'Визначник (за функцією det): {int(round(np.linalg.det(matrix),1))}')
except Exception as exc:
    print(exc)

    
