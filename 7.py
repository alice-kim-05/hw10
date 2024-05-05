number = ''
with open('input7.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if int(line) == 100:
            continue
        else:
            number += line
with open('input7.txt', 'w', encoding='utf-8') as F:
    F.write(number)
