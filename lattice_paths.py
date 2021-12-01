# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 17:06:07 2021

@author: Prital Bamnodkar
"""

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

#     https://projecteuler.net/project/images/p015.png

# How many such routes are there through a 20×20 grid?


def get_grid(size):
    grid = []
    
    for i in range(size + 1):
        row = []
        
        for j in range(size + 1):
            row.append(str(i) + str(j))
        grid.append(row)
        
    return grid

def next_node(grid, node):
    '''

    Parameters
    ----------
    grid : TYPE
        a grid of a specified size.
    i : TYPE
        current row of the current node.
    j : TYPE
        current column of the curent node.

    Returns
    -------
    a list of two coordinates which are horizontally and vertically next to the current point respectively.
    each coordinate is represented by a tuple. 
    None if the node is the last node in a grid.

    '''
    i = node[0]
    j = node[1]
    
    grid_size = len(grid) - 1 # we subtract 1 because we need the lenght of the grid, not the number of points in it. 
    # print('grid size:', grid_size)
    out = []

    if i == grid_size and j == grid_size:
        return None
    
    if j < grid_size:
        out.append((i, j + 1))
        
    if i < grid_size:
        out.append((i + 1, j))
        
    return out

def append_next_nodes_to_paths(grid, paths_list):
    paths = paths_list[:]
    
    for path in paths:
        print('\npaths:', paths)
        print('current path:', path)
        
        current_node = path[-1]
        print('current node:', current_node)
        
        next_nodes = next_node(grid, current_node)
        print('\t next nodes:', next_nodes)
        
        if len(next_nodes) > 1:
            path_copy = path[:]
                        
            path.append(next_nodes[0])
            path_copy.append(next_nodes[1])
            # print(path_copy, '\n')
            
            paths = paths + [path_copy]
        else:
            path.append(next_nodes[0])
            
            
    return paths

def lattice_paths(grid):
    paths = [[(0, 0)]]
        
    while next_node(grid,paths[-1][-1]):
        print('\n', '-' * 5)
        
        paths = append_next_nodes_to_paths(grid, paths)
        print('\n current paths:', paths)
    
    return paths

# grid represented by storing its points in a 2-d list

# grid = [
#     ['00', '01'],
#     ['10', '11'],
# ]

grid = get_grid(2)
result = lattice_paths(grid)

# print(grid)

# print(next_node(grid, (1, 1)))
print('\n' * 2)
print('lattice paths of the grid:', result)
print('total number of paths:', len(result))