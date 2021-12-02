boy, girl = [], []
for i in range(140):
    with open(f'papka\\yob{1880+i}.txt', 'r') as f:
        lines = f.readlines()
        f, m = {}, {}
        for line in lines:
           line = line.replace("\n", '').split(',')
           if line[1] == 'F':
               f[line[0]] = int(line[2])
           else: 
               m[line[0]] = int(line[2])
        girl+=[max(f, key=f.get)]
        boy+=[max(m, key=m.get)]
f,m = {}, {}
for i in girl:
     f[i] = girl.count(i)
for i in boy:
     m[i] = boy.count(i)
f = {i: j for i,j in sorted(f.items(), key = lambda x: x[1],reverse = True)}
m = {i: j for i,j in sorted(m.items(), key = lambda x: x[1],reverse = True)}
[print(f'{i}: {m[i]}') for i in m]
print()
[print(f'{i}: {f[i]}') for i in f]

