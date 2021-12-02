import string
a = string.ascii_lowercase
d,s = {},0
with open('gadsby.txt', 'r') as f:
    lines = f.readlines()
    for i in a:
         k = 0
         for line in lines:
             k += line.lower().count(i)
         s+=k
         d[i] = k
for i in d:
     d[i] = round(d[i]/s*100,3)
d = sorted(d.items(), key = lambda x: x[1], reverse = True)
vv = {i: j for i,j in d[:5]+d[-5:]}
[print(f'{i}: {vv[i]}%') for i in vv]
