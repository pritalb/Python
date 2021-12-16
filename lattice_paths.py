# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 17:06:07 2021

@author: Prital Bamnodkar
"""

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

#     https://projecteuler.net/project/images/p015.png

# How many such routes are there through a 20×20 grid?

# formula for total cases = (width + heigh)! / (width! * height!)

# divide the grid into 2 parts at the bottom-left to top-right diagonal
# we know the starting point - (0, 0) and the ending point (n, n) where n is the grid size
# so instead of getting paths from starting node to ending node, we can divide the grid into 2 triangles
# and get paths from the top and the end to the diagonal nodes respectively.
# then we add them together to get full paths.

from math import factorial

# Top half of the Grid
def grid_top_half(grid_size):
    out = []
    
    for i in range(grid_size + 1):
        row = []
        
        for j in range(grid_size - i + 1):
            row.append((i, j))
        out.append(row)
    return out

# adjacent nodes are one to the right and the one below a node
def get_adjacent_node_top_half(grid_size, node):
    i = node[0] # row
    j = node[1] # column

    if i + j >= grid_size:
        return None

    node_right = (i, j + 1)
    node_below = (i + 1, j)
    return [node_below, node_right]

# returns a dictionary of paths that lead to a node.
# node -> list of paths
def node_path_dict_top_half(grid_top_half, grid_size):
    path_dict = {
        (0, 0) : [ [(0, 0)], ],
    }

    nodes_in_grid_top = []
    for row in grid_top_half:
        for node in row:
            nodes_in_grid_top.append(node)

    for node in nodes_in_grid_top:
        adjacent_nodes = get_adjacent_node_top_half(grid_size, node)

        if not adjacent_nodes:
            continue

        for adjacent_node in adjacent_nodes:
            path_upto_current_node = path_dict[node][0] + [adjacent_node]

            if adjacent_node in path_dict.keys():
                paths_upto_now = path_dict[adjacent_node] # does not include current node
                
                # for path in paths_upto_now:
                path_dict[adjacent_node].append(path_upto_current_node)
            else:
                path_dict[adjacent_node] = [path_upto_current_node]
    return path_dict

def lattice_paths_top(grid_size):
    grid_top = grid_top_half(grid_size)
    paths = node_path_dict_top_half(grid_top, grid_size)

    # print(*paths.items(), sep='\n')
    return paths



# Bottom half of the grid
def grid_bottom_half(grid_size):
    out = []
    
    for i in range(grid_size + 1):
        row = []
        
        for j in range(grid_size - i, grid_size + 1):
            row.append((i, j))
        out.append(row)    
    return out

# adjacent nodes are one to the left and the one above a node
def get_adjacent_node_bottom_half(grid_size, node):
    i = node[0] # row
    j = node[1] # column

    if i + j <= grid_size:
        return None

    node_left = (i, j - 1)
    node_above = (i - 1, j)
    return [node_above, node_left]

# returns a dictionary of paths that lead to a node.
# node -> list of paths
def node_path_dict_bottom_half(grid_bottom_half, grid_size):
    last_node = (grid_size, grid_size)
    path_dict = {
        last_node : [ [last_node], ],
    }

    nodes_in_grid_bottom = []
    for row in grid_bottom_half:
        for node in row:
            nodes_in_grid_bottom.append(node)
    nodes_in_grid_bottom.reverse()

    for node in nodes_in_grid_bottom:
        adjacent_nodes = get_adjacent_node_bottom_half(grid_size, node)

        if not adjacent_nodes:
            continue

        for adjacent_node in adjacent_nodes:
            path_upto_current_node = path_dict[node][0] + [adjacent_node]

            if adjacent_node in path_dict.keys():
                paths_upto_now = path_dict[adjacent_node] # does not include current node
                
                # for path in paths_upto_now:
                path_dict[adjacent_node].append(path_upto_current_node)
            else:
                path_dict[adjacent_node] = [path_upto_current_node]
    return path_dict


def get_diagonal_nodes(grid_size):
    nodes = []

    for i in range(grid_size + 1):
        nodes.append((i, grid_size - i))
    return nodes

def lattice_paths_bottom(grid_size):
    grid_bottom = grid_bottom_half(grid_size)
    paths = node_path_dict_bottom_half(grid_bottom, grid_size)

    # print(*paths.items(), sep='\n')
    return paths

def lattice_paths(grid_size):
    paths_top = lattice_paths_top(grid_size)
    paths_bottom = lattice_paths_bottom(grid_size)
    diagonal_nodes = get_diagonal_nodes(grid_size)
    full_paths = []

    for node in diagonal_nodes:
        paths_from_top = paths_top[node]
        paths_from_bottom = paths_bottom[node]

        for path_top in paths_from_top:
            for path_bottom in paths_from_bottom:
                path_bottom_copy = path_bottom[:]
                path_bottom_copy.reverse()

                full_paths.append(path_top + path_bottom_copy[1:])

    return full_paths   


# Test Functions
def test_grid_top_half(grid_size):
    print('top:', *grid_top_half(grid_size), sep=('\n'))

def test_grid_bottom_half(grid_size):
    print('bottom:', *grid_bottom_half(grid_size), sep=('\n'))

def test_get_adjacent_node_top_half(grid_size):
    nodes = [
        (0, 0),
        (1, 2),
        (0, 2),
        (1, 1)
    ]

    for node in nodes:
        print('nodes adjacent to', node, ':', get_adjacent_node_top_half(grid_size, node))

def test_get_adjacent_node_bottom_half(grid_size):
    nodes = [
        (2, 2),
        (1, 1),
        (2, 1)
    ]

    for node in nodes:
        print('nodes adjacent to', node, ':', get_adjacent_node_bottom_half(grid_size, node))

def correct_lattice_paths_num(height, width):
    return int(factorial(width + height) / (factorial(width) * factorial(height)))

def test_lattice_paths():
    test_cases = [
        1, 2, 3,
    ]

    for test_case in test_cases:
        paths = lattice_paths(test_case)
        expected_paths_num = correct_lattice_paths_num(test_case, test_case)
        actual_paths_num = len(paths)

        print('\n', '_____' * 5)
        print('List of lattice paths: ', *paths, sep='\n')
        print('Grid size:', test_case, '\nExpected number of paths:', expected_paths_num, '\n Actual number of paths found:', actual_paths_num)

test_lattice_paths()