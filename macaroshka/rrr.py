import array
l = []
p = 0
o = 0
mas = []
for i in range(20):
  row = []
  p = o

  for j in range(20):
    row.append(p)
    o = p
    if p == 1:
        p = 0

    elif p == 0:
        p = 1
    
  mas.append(row)
print(mas)
