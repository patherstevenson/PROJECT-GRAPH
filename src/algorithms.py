# AUTHOR : Pather Stevenson, Larafi Zakaria

import queue as q
import numpy as np
import networkx as nx

# Algorithms module

## Fonctions annexes

# recherche de la plus petite couleur disponible pour colorier s dans g par rapport à l_color
def plusPetitCouleur(g,l_color,s):
    voisins = list(g.neighbors(s))
    couleur_voisins = []

    # remplissage de la liste des couleurs des voisins du sommet parcouru
    for v in voisins:
        couleur_voisins+= [l_color[v]]

    # recherche de la plus petite couleur disponible
    i = 1
    while i in couleur_voisins:
        i += 1

    return i

# obtention de la liste des degrés des sommets de g dans l'ordre décroissant
def degre_decroissant(g):
    return [x[0] for x in sorted(g.degree, key=lambda x: x[1], reverse=True)]

# obtention du DSAT MAX pour les sommets dans sommets, de g
def DSAT_MAX(g,l_color,sommets):
    dsat = {s : 0 for s in list(g.nodes())}
    dsat_max = 0
    dsat_max_s = sommets[0]

    for s in sommets:

        # si le sommet s actuellement parcouru n'a pas encore de couleur attribué
        if l_color[s] == 0:
            voisins = list(g.neighbors(s))
            degre_sat = 0

            # recherche degre sat max 
            for v in voisins:
                if l_color[v] > 0:
                    degre_sat += 1
            dsat[s] = degre_sat

            # mise à jour du DSAT_MAX
            if dsat[s] > dsat_max:
                dsat_max = dsat[s]
                dsat_max_s = s

    return dsat_max_s

def parcours_en_largeur_ite(graphe, sommet,visited=[]):
    res = np.array([], dtype=int)
    if (visited == []):
        visited = [False for i in range(graphe.number_of_nodes())]
    to_visit = q.Queue()
    to_visit.put(sommet)

    while (not to_visit.empty()):
        current_sommet = to_visit.get()
        if not visited[current_sommet]:
            res = np.append(res,current_sommet)
            visited[current_sommet] = 1
            for neighbors in list(graphe.neighbors(current_sommet)):
                if not visited[neighbors]:
                    to_visit.put(neighbors)
    return res

def composantes_connexes(graphe):
    res = []
    visited = [False for i in range(graphe.number_of_nodes())]
    for sommet in list(graphe.nodes()):
        if not visited[sommet]:
            res.append(parcours_en_largeur_ite(graphe,sommet,visited))
    return res

## Algorithme glouton

def glouton(g,l_color):
    sommets = list(g.nodes())
    l_color_res = l_color

    for s in sommets:
        l_color_res[s] = plusPetitCouleur(g,l_color,s)

    return l_color_res

## Heuristique DSATUR

def DSATUR(g,l_color):

    while 0 in l_color.values(): # 0 = sommet pas colorier

        dsat_max = DSAT_MAX(g,l_color,degre_decroissant(g))

        l_color[dsat_max] = plusPetitCouleur(g,l_color,dsat_max)

    return l_color
