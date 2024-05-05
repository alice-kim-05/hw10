with open('input6.txt', 'r', encoding='utf-8') as f:
    with open('output6.txt', 'w', encoding='utf-8') as F:
        try:
            ch = int(f.readline())
            line = f.readlines()
            if len(line) == ch:
                F.write('YES')
            else:
                F.write('NO')
        except Exception:
            F.write('ERROR')
            