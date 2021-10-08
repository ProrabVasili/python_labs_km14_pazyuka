salary_list = [7.3, 8.5, 11, 12.7, 15.2, 21.12, 27.35]
salary_list = [[i, round(i*1.3,2), round(i*0.3,2)] for i in salary_list]
print('Salary table:')
for i in range(len(salary_list)):
    for j in range(3):
        print(str(salary_list[i][j]).ljust(8), end='')
    print()