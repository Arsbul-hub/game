n1 = 0
n2 = 2
h = [2,5,7,1,9,6,8,3,4]
for i in range(len(h)):


    if  h[i] > n1 and h[i] < n2:
        n1 += 1
        n2 += 1
        print(h[i])
