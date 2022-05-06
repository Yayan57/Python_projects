from array import *
rows, cols = (8, 8)
arr = [[0 for i in range(cols)] for j in range(rows)]

for i in range(cols):
    if i% 2:
        for j in range(rows):
            if j % 2:
                arr[i][j] = 'black'
            else:
                arr[i][j] = 'white'
    else:
        for j in range(rows):
            if j % 2:
                arr[i][j] = 'white'
            else:
                arr[i][j] = 'black'



