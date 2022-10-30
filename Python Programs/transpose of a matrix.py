a=[[1,2],
   [7,10],
   [15,12]]
transpose = [[0,0,0],
             [0,0,0]]
for i in range (len(a)):
    for j in range(len(a[0])):
                   transpose[j][i]=a[i][j]
for t in transpose:
    print(t)
