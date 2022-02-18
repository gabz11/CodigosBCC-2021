a = []
for x in range(4):
    a.append('.')
cont = len(a)
for x in range(len(a)):
    lin = []
    for c in range(len(a)):
        while c < cont:
            if c == 0:
                lin.append('X')
            if c == 1:
                lin.append('O')
            if c == 2:
                lin.append('|')
            if c == 3:
                lin.append('@')
            a.append(lin)
            cont -= 1
print(a)