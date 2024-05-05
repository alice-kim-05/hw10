S = 0
st = []
with open('input8.txt', 'r', encoding='utf-8') as f:
    with open('output8.txt', 'w', encoding='utf-8') as F:
        year = f.readlines()
        if len(year) == 366:
            feb = 29
        else:
            feb = 28
        months = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        s = 0
        f = 0
        for day in months:
            f += day
            m = year[s:f]
            s += day
            for d in m:
                S += int(d)
            ev = int(S / day)
            S = 0
            st.append(ev)
        for i in st:
            k = str(i)
            F.write(k + '\n')
