sl = [7.3, 8.5, 11, 12.7, 15.2, 21.12, 27.35]
sai = list(map(lambda x: round(x*1.3,2), sl))
si = list(map(lambda x,y: round(x-y,2), sai,sl))
print('Salary table:')
for i in range(len(si)):
    print(sl[i],sai[i],si[i])
