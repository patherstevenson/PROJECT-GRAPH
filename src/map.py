# AUTHOR : Pather Stevenson, Larafi Zakaria

import sys
import numpy as np
import networkx as nx
import algorithms

# Map module

def main(fileIn, fileOut) :
    stream = open(fileIn, "r")
    edges = stream.readlines()
    stream.close()

    G = nx.Graph()
    d =  {}

    i = 0

    for e in edges:
        line = e.split(" ")
        assert(len(line) == 2)

        a = line[0]
        b = line[1].replace("\n","")

        if a not in d:
            d[a] = i
            i += 1
        if b not in d:
            d[b] = i
            i +=1

        G.add_edge(d[a],d[b])

    l_color = {s : 0 for s in list(G.nodes())}

    color_list = algorithms.DSATUR(G,l_color)

    stream = open(fileOut, "w")

    for k in color_list:
        stream.write('{0} {1}\n'.format(list(d.keys())[list(color_list.keys()).index(k)],color_list[k]-1))
    stream.close()


def usage(argv):
    print(f"Usage: python3 {argv[0]} -i input.txt -o output.txt")

if __name__ == "__main__":
    if len(sys.argv) == 5 and sys.argv[1] == '-i' and sys.argv[3] == '-o':
        main(sys.argv[2],sys.argv[4])
    else:
        usage(sys.argv)

