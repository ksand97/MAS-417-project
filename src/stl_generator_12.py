import numpy as np
from stl import mesh


def stl_generator(y, stockname):

    f = max(y)
    k = 12/f
    
    
    y1=k*y[0]
    y2=k*y[1]
    y3=k*y[2]
    y4=k*y[3]
    y5=k*y[4]
    y6=k*y[5]
    y7=k*y[6]
    y8=k*y[7]
    y9=k*y[8]
    y10=k*y[9]
    y11=k*y[10]
    y12=k*y[11]



    points = np.array([
        [0,0,0], #0
        [0,y1,0], #1
        [1,y2,0], #2
        [2,y3,0], #3
        [3,y4,0], #4
        [4,y5,0], #5
        [5,y6,0], #6
        [6,y7,0], #7
        [7,y8,0], #8
        [8,y9,0], #9
        [9,y10,0], #10
        [10,y11,0], #11
        [11,y12,0], #12
        [11,0,0], #13
        [10,0,0], #14
        [9,0,0], #15
        [8,0,0], #16
        [7,0,0], #17
        [6,0,0], #18
        [5,0,0], #19
        [4,0,0], #20
        [3,0,0], #21
        [2,0,0], #22
        [1,0,0], #23

        [0,0,1], #24
        [0,y1,1], #25
        [1,y2,1], #26
        [2,y3,1], #27
        [3,y4,1], #28
        [4,y5,1], #29
        [5,y6,1], #30
        [6,y7,1], #31
        [7,y8,1], #32
        [8,y9,1], #33
        [9,y10,1], #34
        [10,y11,1], #35
        [11,y12,1], #36
        [11,0,1], #37
        [10,0,1], #38
        [9,0,1], #39
        [8,0,1], #40
        [7,0,1], #41
        [6,0,1], #42
        [5,0,1], #43
        [4,0,1], #44
        [3,0,1], #45
        [2,0,1], #46
        [1,0,1], #47

        
    ])

    triangles = np.array([
        [0,2,1],
        [0,23,2],
        [23,3,2],
        [23,22,3],
        [22,4,3],
        [22,21,4],
        [21,5,4],
        [21,20,5],
        [20,6,5],
        [20,19,6],
        [19,7,6],
        [19,18,7],
        [18,8,7],
        [18,17,8],
        [17,9,8],
        [17,16,9],
        [16,10,9],
        [16,15,10],
        [15,11,10],
        [15,14,11],
        [14,12,11],
        [14,13,12],

        [0,24,25],
        [0,25,1],
        [25,2,1],
        [25,26,2],
        [26,3,2],
        [26,27,3],
        [27,4,3],
        [27,28,4],
        [28,5,4],
        [28,29,5],
        [29,6,5],
        [29,30,6],
        [30,7,6],
        [30,31,7],
        [31,8,7],
        [31,32,8],
        [32,9,8],
        [32,33,9],
        [33,10,9],
        [33,34,10],
        [34,11,10],
        [34,35,11],
        [35,12,11],
        [35,36,12],

        [37,12,36],
        [37,13,12],

        [0,37,24],
        [0,13,37],

        [24,26,25],
        [24,47,26],
        [47,27,26],
        [47,46,27],
        [46,28,27],
        [46,45,28],
        [45,29,28],
        [45,44,29],
        [44,30,29],
        [44,43,30],
        [43,31,30],
        [43,42,31],
        [42,32,31],
        [42,41,32],
        [41,33,32],
        [41,40,33],
        [40,34,33],
        [40,39,34],
        [39,35,34],
        [39,38,35],
        [38,36,35],
        [38,37,36],

    ])

    shape = mesh.Mesh(np.zeros(triangles.shape[0], dtype=mesh.Mesh.dtype))

    for i, f in enumerate(triangles):
        for j in range(3):
            shape.vectors[i][j] = points[f[j], :]




    shape.save(stockname+".stl")

    print("Success! Your STL and plot image was generated. \nThey can be found as "+stockname+".stl and "+stockname+".png in the current workspace")