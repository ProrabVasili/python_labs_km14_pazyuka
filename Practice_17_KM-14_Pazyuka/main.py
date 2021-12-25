from factorial import factorial
from exp_root import exponentiation
from exp_root import root
from logarithm import logarithm

def main():
    r = ['fact','root3','root2','exp3','exp2','log','lg','ln']
    print(f"Functions available to you: {', '.join(r)}")
    while True:
        try:
            func = input('Select a function: ')
            if func not in r:
                raise Exception('You entered incorrect answer!')
            break
        except Exception as exc:
            print(exc)
    if func == 'fact':
        while True:
            try:
                n = input('Input natural number or 0: ')
                if n.isdigit() == False :
                    raise Exception('You entered incorrect answer!')
                n = int(n)
                break
            except Exception as exc:
                print(exc)
    elif func in r[1:5]:
        while True:
            try:
                n = float(input('Input number: '))
                break
            except ValueError:
                print("You didn't entered number!")
    else:
        while True:
            try:
                a = float(input('Input the logarithm argument: '))
            except ValueError:
                print('You entered a non-positive number!')
                continue
            try:
                if a<0:
                    raise Exception('You entered negative number!')
                elif a == 0:
                    raise Exception('You entered 0!')
                break
            except Exception as exc:
                print(exc)
    if func == 'log':
        while True:
            try:
                b = float(input('Input the base of the logarithm: '))
            except ValueError:
                print('You entered a non-positive number!')
                continue
            try:
                if b < 0:
                    raise Exception('You entered negative number!')
                elif b == 0:
                    raise Exception('You entered 0! This is wrong!')
                elif b == 1:
                    raise Exception('You entered 1! This is wrong!')
                break
            except Exception as exc:
                print(exc)
    if func == 'fact':
        print(f'Factorial {n}: {factorial.fact(n)}')
    elif func == 'root3':
        print(f'Cube root {n}: {root.root3(n)}')
    elif func == 'root2':
        print(f'Square root {n}: {root.root2(n)}' if n>=0 else root.root2(n))
    elif func == 'exp3':
        print(f'{n} cubed: {exponentiation.exp3(n)}')
    elif func == 'exp2':
        print(f'{n} squared: {exponentiation.exp2(n)}')
    elif func == 'log':
        print(f'Logarithm {a} with base {b}: {logarithm.log(a,b)}')
    elif func == 'lg':
        print(f'Decimal logarithm {a}: {logarithm.lg(a)}')
    else:
        print(f'Natural logarithm {a}: {logarithm.ln(a)}')

if __name__ == "__main__":
    main()