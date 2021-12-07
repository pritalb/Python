# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 17:06:07 2021

@author: Prital Bamnodkar
"""

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

#     https://projecteuler.net/project/images/p015.png

# How many such routes are there through a 20×20 grid?


def get_grid(size):
    '''

    Parameters
    ----------
    size : int
        DESCRIPTION.
        the number of unit lenghts of the grid, not the number of points.
        
    Returns
    -------
    grid : list
        DESCRIPTION.
        a list of lists. each sublist represents a row of points represented by a tuple.
    '''
    grid = []
    
    for i in range(size + 1):
        row = []
        
        for j in range(size + 1):
            row.append(str(i) + str(j))
        grid.append(row)
        
    return grid

def adjacent_nodes_dict(grid):
    '''

    Parameters
    ----------
    grid : list
        DESCRIPTION.
        a grid represented as a list of rows
        
    Returns
    -------
    adjacent_nodes : dictionary
        DESCRIPTION.
        a dictionary of nodes next to a particular node.
        node -> [node to right, node below]
    '''
    grid_size = len(grid)
    adjacent_nodes = {}
    
    for i in range(grid_size):
        for j in range(grid_size):
            node = (i, j)
            
            if node not in adjacent_nodes.keys():
                adjacent_nodes[node] = next_node(grid, node)
                
    return adjacent_nodes

def next_node(grid, node):
    '''

    Parameters
    ----------
    grid : TYPE
        a grid of a specified size.
    node : TYPE
        a point/node in the grid

    Returns
    -------
    a list of two coordinates which are horizontally and vertically next to the current point respectively.
    each coordinate is represented by a tuple. 
    None if the node is the last node in a grid.

    '''
    i = node[0] # row
    j = node[1] # column
    
    # we subtract 1 because we need the lenght of the grid, not the number of points in it.
    grid_size = len(grid) - 1  
    out = []

    if i == grid_size and j == grid_size:
        return None
    
    if j < grid_size:
        out.append((i, j + 1))
        
    if i < grid_size:
        out.append((i + 1, j))
        
    return out


def lattice_paths(grid):
    '''

    Parameters
    ----------
    grid : List
        DESCRIPTION.
        a grid of size n
        
    Returns
    -------
    List
        DESCRIPTION.
        a list of paths that lead to the last node (n, n) of the grid
    '''
    
    adjacent_nodes = adjacent_nodes_dict(grid)
    grid_size = len(grid) - 1
    last_node = (grid_size, grid_size)
 
    # stores list of paths that lead to nodes.   node -> list of paths where a path itself is a list of nodes
    path_dict = {
        (0, 0) : [[(0, 0)]]
        }
    
    paths = []
    for node in adjacent_nodes.keys():
        # print('\n', '- - - - -' * 5, '\n')

        if node in path_dict.keys():
            paths = path_dict[node]
        
        next_nodes = adjacent_nodes[node]
        # print('currently on node:', node)
        
        if not next_nodes:
            break
        
        for next_node in next_nodes:
            if len(paths) > 1:
                for path in paths:
                    appended_path = path + [next_node]

                    if next_node in path_dict.keys():
                        path_dict[next_node].append(appended_path)
                    else:
                        path_dict[next_node] = [appended_path]
            else:
                path = paths[0]
                appended_path = path + [next_node]
                
                if next_node in path_dict.keys():
                    path_dict[next_node].append(appended_path)
                else:
                    path_dict[next_node] = [appended_path]
        
    return path_dict[last_node]
        
grid = get_grid(20)
result = lattice_paths(grid)

print('\n' * 5)
# print('lattice paths of the grid:\n', *result, sep='\n')
print('total number of paths:', len(result))