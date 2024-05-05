e = 0
d = 0
try:
    with open('input5.txt', 'r', encoding='utf-8') as f:
        a = int(f.readline())
        b = int(f.readline())
        c = int(f.readline())
        try:
            d = a / b
        except ZeroDivisionError:
            print('На ноль делить нельзя')
        e = d + c
except ValueError:
    print('В файле не только числа')
with open('output5.txt', 'w', encoding='utf-8') as F:
    F.write(str(e))
