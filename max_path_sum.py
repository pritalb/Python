# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 17:43:02 2021

@author: Prital Bamnodkar
"""

# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

#    3
#   7 4
#  2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

#                           75
#                          95 64
#                        17 47 82
#                      18 35 87 10
#                    20 04 82 47 65
#                  19 01 23 75 03 34
#                88 02 77 73 07 63 67
#              99 65 04 28 06 16 70 92
#            41 41 26 56 83 40 80 70 33
#          41 48 72 33 47 32 37 16 94 29
#        53 71 44 65 25 43 91 52 97 51 14
#      70 11 33 28 77 73 17 78 39 68 17 57
#    91 71 52 38 17 14 91 43 58 50 27 29 48
#  63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

visited_nodes = {}
def paths(pyramid, i, j, visited_nodes): # i and j to keep track of which node we are on. i => row in the pyramid and j => node in that row
    node = pyramid[i][j]
    node_index = str(i) + str(j)
    pyramid_size = len(pyramid)
    
    # the pyramid gets smaller for every iteration.
    # the pyramid with the current node at top gets smaller.
    # e.g. every node forms its own pyramid since there are other nodes under it. the lower the node,
    # the fewer nodes it would have under it and the smaller its respective pyramid would be.
    node_pyramid_size = pyramid_size - i
    
    if node_index in visited_nodes.keys():
        return visited_nodes[node_index]
    else:
        if node_pyramid_size <= 1:
            out = [node]
        elif node_pyramid_size == 2:
            out = [
                [node] + paths(pyramid, i + 1, j, visited_nodes),
                [node] + paths(pyramid, i + 1, j + 1, visited_nodes)
            ]
        else:
            try:
                adjacent_node_1_paths = paths(pyramid, i + 1, j, visited_nodes)
                adjacent_node_2_paths = paths(pyramid, i + 1, j + 1, visited_nodes)
                 
                out = []
                
                for path in adjacent_node_1_paths:
                    out.append([node] + path)
                    
                for path in adjacent_node_2_paths:
                    out.append([node] + path)
            except:
                print('error at node:', node, 'i:', i, 'j:', j)
                
    visited_nodes[node_index] = out
    return out

pyramid = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
]

pyramid_paths = paths(pyramid, 0, 0, visited_nodes)
print(max(list(map(sum, pyramid_paths))))