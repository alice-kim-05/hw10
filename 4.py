lines = ''
with open('input4.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if len(line) > 21:
            lines += line
with open('output4.txt', 'w', encoding='utf-8') as F:
    F.write(lines)
