import array
l = []
p = 0
mas = []
for i in range(5):
    if p == 1:
        l.append(p)
        p = 0
    if p == 0:
        l.append(p)
        p = 1
    
    if i == 7:
        p = 1
        l.append(p)
    l = []
    mas =[]
    for j in range(8):
        mas.append(l)
print(mas)
