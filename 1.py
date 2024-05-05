with open('input1.txt', 'r', encoding='utf-8') as f:
    a = f.readline()
with open('output1.txt', 'w', encoding='utf-8') as F:
    F.write(a.upper())
