import os

os.mkdir(f'simple')
with open('input9.txt', 'r', encoding='utf-8') as f:
    with open('simple\\output9.txt', 'w', encoding='utf-8') as F:
        line = f.readlines()
        for i in range(1, len(line), 2):
            F.write(line[i])
