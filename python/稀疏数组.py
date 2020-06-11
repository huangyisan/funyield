import numpy as np

'''
0 0 0 0 0 0 0
0 1 0 0 0 0 0
0 0 2 0 1 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 2 0 0 0
0 0 0 0 0 0 0

'''

chess_map = [[0 for i in range(7)] for j in range(7)]
chess_map[1][1] = 1
chess_map[2][2] = 2
chess_map[2][4] = 1
chess_map[5][3] = 2

for i in chess_map:
    for j in i:
        print(j, end="\t")
    print("")

chess_sparse_map = [[7,7,0]]

for i in enumerate(chess_map):
    for j in enumerate(i[-1]):
        if j != 0:
            print(j)




