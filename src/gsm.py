# AUTHOR : Pather Stevenson, Larafi Zakaria

import sys
import networkx as nx
import algorithms

# GSM module

def main(filename,output):
    stream = open(filename, "r")
    edges = stream.readlines()
    stream.close()

    G = nx.Graph()

    for e in edges:
        line = e.split(" ")
        assert(len(line) == 2)

        x = int(line[0])-1
        y = int(line[1])-1

        G.add_edge(x,y)

    comp_connexes = algorithms.composantes_connexes(G)

    res = []

    for comp_c in comp_connexes:
        l_color = {s : 0 for s in comp_c}
        res += [algorithms.DSATUR(G.subgraph(comp_c),l_color)]

    stream = open(output, "w")

    for d in res:
        for k in d:
            stream.write('{0} {1}\n'.format(k+1,d[k]-1))

    stream.close()


def usage(argv):
    print(f"Usage: python3 {argv[0]} -i input.txt -o output.txt")

if __name__ == "__main__":
    if len(sys.argv) == 5 and sys.argv[1] == '-i' and sys.argv[3] == '-o':
        main(sys.argv[2],sys.argv[4])
    else:
        usage(sys.argv)
