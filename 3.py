lines = ''
with open('input3.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lines += line[0]
with open('output3.txt', 'w', encoding='utf-8') as F:
    F.write(lines)
