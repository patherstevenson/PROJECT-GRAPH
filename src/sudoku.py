# AUTHOR : Pather Stevenson, Larafi Zakaria

import sys
import numpy as np
import networkx as nx
import algorithms

# Sudoku module

# Graphe qui représente la grille de sudoku 9x9

valid_value = [i for i in range(1,10)]

G = nx.sudoku_graph(3)

color_list = {s : 0 for s in list(G.nodes())}

grid = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]

dd = {}


# Main fonction

def main(filename):
    fill_graph_from_file(filename)
    affect_color_from_presolve()
    solve_grid_from_filled_color_list()
    attrib_last_unknowed_color()
    for l in grid:
        print(l)
        # print("\n")

def fill_graph_from_file(filename):
    col = 1
    stream = open(filename, "r")
    values = stream.readlines()

    for v in values:
        line = v.split(" ")
        assert(len(line) == 3)

        x = int(line[0]) - 1
        y = int(line[1]) - 1
        val = int(line[2].replace("\n",""))

        assert(val in valid_value)

        grid[y][x] = val

        if val not in dd.values():
            dd[col] = val
            color_list[(y*9) + x] = col
            col += 1
        else:
            color_list[(y*9) + x] = list(dd.keys())[list(dd.values()).index(val)]

def affect_color_from_presolve():
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                color = color_list[(y*9) + x]
                if color in dd:
                    grid[y][x] = dd[color]

def solve_grid_from_filled_color_list():
    global color_list
    color_list = algorithms.DSATUR(G,color_list)

    for y in range(9):
        for x in range(9):
            color = color_list[(y*9) + x]
            if color in dd:
                grid[y][x] = dd[color]

def attrib_last_unknowed_color():
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                voisins = G.neighbors((y*9) + x)
                voisins_value = [dd[color_list[x]] for x in voisins if color_list[x] in dd]
                possible_value = [x for x in valid_value if x not in voisins_value]
                if len(possible_value) == 1:
                    grid[y][x] = possible_value

                # dd[color_list[(y*9)+x]] = grid[y][x]

if __name__ == "__main__":
    main(sys.argv[1])
