lines = ''
with open('input2.txt', 'r', encoding='utf-8') as f:
    for line in f:
        first = line[0]
        if first == 'a' or first == 'A':
            lines += line
with open('output2.txt', 'w', encoding='utf-8') as F:
    F.write(lines)
