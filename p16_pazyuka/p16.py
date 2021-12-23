while True:
    try:
        n = input('Enter natural number, which divisible by 16 and in [16;1280]: ')
        if n.isdigit() == False:
            raise Exception('You entered non-natural number')
        n = int(n)
        if n not in range(16,1281):
            raise Exception('You entered number, which not in [16;1280]')
        elif n%16!=0:
            raise Exception('You entered number, which not divisible by 16')
        break
    except Exception as exc:
        print(exc)

while True:
    try:
        tf = input('Do you want to use a decorator?(True/False) ')
        if tf not in ['True', 'False']:
            raise Exception('You entered incorrect answer')
        break
    except Exception as exc:
        print(exc)
def decorator(tf):
    def wrap(func):
        def fun(*args):
            if tf == 'True':
                return [[tuple(j[4*k+i] for i in range(4)) for k in range(4)] for j in func(*args)]
            else:
                return func(*args)
        return fun
    return wrap

@decorator(tf)
def pages(n):
    a = [j for i in [(16*(k+1)-i, i+1+16*k)[::(-1)**i] for k in range(n//16) for i in range(8)] for j in i]
    return [[a[16*j+i] for i in range(16)] for j in range(n//16)]
    
"""
функція-генератор
"""
@decorator(tf)
def gen(n):
    for k in range(n//16):
        a = [j for i in [(16*(k+1)-i, i+1+16*k)[::(-1)**i]  for i in range(8)] for j in i]
        yield [a[i] for i in range(16)]
print(pages(n))
print()
print([*gen(n)])
print()
print(f'Number of copybook: {n//16}')