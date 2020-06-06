import array
l = []
p = 0
for i in range(8):
    if p == 0:
        l.append(1)
        p = 1
    if p == 1:
        l.append(0)
        p = 0
    mas = []

    for j in range(8):
        mas.append(l)
print(mas)
