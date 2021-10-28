vv = input('Введіть коефіцієнти a,b та c (через пробіл):').split()
try:
    vv = list(map(float,vv))
    try:
        if len(vv)>3:
            raise Exception('Ви ввели більше трьох коефіцієнтів!')
        elif len(vv)<3:
            raise Exception('Ви ввели менше трьох коефіцієнтів!')
        if vv[0]==0:
            raise Exception('Перший коефіцієнт (а) не повинен бути рівним нулю!')
        d = (vv[1]**2-4*vv[0]*vv[2])
        if d<0:
            raise Exception('Дискримінант менше нуля! Рівняння дійсних коренів не має')
        n,k = -vv[1]/(2*vv[0]), -d**0.5/(2*vv[0])
        print(f'Рівняння має 2 корені: {n-k} та {n+k}' if k!=0 else f'Рівняння має один корінь: {n}')
    except Exception as exc:
        print(exc)
except ValueError:
    print('Коефіцієнти повинні складатись лише з чисел!')
