import array
l = []
p = 0
o = 0
mas = []
for i in range(8):
  row = []
  p = o
  print("ffffffffff:  " + str(o))
  for j in range(8):
    row.append(p)
    o = p
    if p == 1:
        p = 0

    elif p == 0:
        p = 1
    
  mas.append(row)
print(mas)
