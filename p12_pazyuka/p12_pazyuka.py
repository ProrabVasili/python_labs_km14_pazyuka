dirs = [
    ( 'folder1',
        [
            'file1',
            ( 'folder2', 
                [
                    'file2',
                    'file3'
                ] 
            ),
            ( 'folder3', 
                [
                    'file3', 
                    'file4',
                    ('folder4', ['file3'])
                ] 
            ),
            'file5'
        ]
    )
]
b = dirs.copy()
# ВАШ КОД ТУТ
from functools import reduce
sum=[]
def per(dirs):
    return [j for i in dirs for j in i if type(j)==str]
def allelem(lst, word):
    global sum
    for element in lst:
        if type(element) == list or  type(element) == tuple:
            allelem(element, word)
        else:
            sum += [f'{element}']
    return sum
def search(dirs, filename, way = ''):
    total = []
    if filename not in allelem(b,filename) or filename in per(b):
        return []
    else:
        if type(dirs) == tuple:
            way += f'/{dirs[0]}/'
            dirs = dirs[1]
            total += reduce(lambda total, por: total + search(por, filename,way), dirs, [])
        elif type(dirs) == list:
            total += reduce(lambda total, por: total + search(por, filename,way), dirs, [])
        elif filename == dirs:
            total += [f'{way}{filename}']
        return total
# ПЕРЕВІРКА

print(search(dirs, 'file1'))
print(search(dirs, 'file2'))
print(search(dirs, 'file3'))
print(search(dirs, 'file4'))
print(search(dirs, 'file5'))
print(search(dirs, 'file6'))
print(search(dirs, 'folder1'))

assert search(dirs, 'file1') == ['/folder1/file1'], 'Failed test for file1'
assert search(dirs, 'file2') == ['/folder1//folder2/file2'], 'Failed test for file2'
assert search(dirs, 'file3') == ['/folder1//folder2/file3', '/folder1//folder3/file3', '/folder1//folder3//folder4/file3'], 'Failed test for file3'
assert search(dirs, 'file4') == ['/folder1//folder3/file4'], 'Failed test for file4'
assert search(dirs, 'file5') == ['/folder1/file5'], 'Failed test for file5'
assert search(dirs, 'file6') == [], 'Failed test for file6'
assert search(dirs, 'folder1') == [], 'Failed test for folder1'
print('All tests good!')
