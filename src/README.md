# Compte-rendu du code

## Etat du code

Nous avons réalisé l'implémentation de tous les algorithmes glouton et DSATUR.
Ainsi que toutes fonctions qui permettent leur bon fonctionnement.
Ceux-ci sont dans le fichier algorithms.py

Nous avons remplacer l'utilisation d'une liste pour dictionnaire pour l'argument l_color des algorithmes.
Ce qui permet l'utilisation direct de ceux-ci pour les trois problèmes.

Nous avons réussi l'implémentation complète qui permet la résolution du problème de map et gsm.
Hors pour sudoku nous rencontrons le problème suivant :

	- Nous générons un graphe qui représente une grille de sudoku vide 9x9 à l'aide de la commande networkx.sudoku_graph(3)
	- Nous affectons une couleur unique à chaque valeur déjà présente dans la grille de jeu donnée par le fichier input
	- Nous colorions partiellement notre graphe en fonction des affectations faite à l'étape précédente
	- Nous utilisons l'algorithme DSATUR pour trouver une coloration à partir du graphe et de la pré coloration faite
	- Nous affectons les valeurs correspondante aux couleurs que l'on connaît déjà grâce à grille pré remplie et le dictionnaire de coloration donné par DSATUR

Ainsi Nous obtenons une grille de jeu presque résolue. L'on se rend compte qu'il y a donc des fois plusieurs possibilité. Et que le nombre chromatique n'est pas de 9.
Ce qui a pour effet qu'une valeur peut être affecter à plusieurs couleurs ce qui complique l'approche que l'on peut faire à cette étape pour résoudre la grille.

Il faudrait trouver les bonnes affectations (couleur -> valeur) des valeurs possibles pour les cases avec la valeur 0 (Valeur valide 1 à 9).
Et qui permettent une grille résolue valide.

Nous avons tenter une approche où l'on attribuer en fonction des voisins du sommet correspondant à la case.
Hors cela a eu pour effet d'avoir une grille où l'on se pouvait pas mettre de valeur car cela donnerait une grille de jeu non valide
avec par exemple une valeur présente deux fois dans un carré, ou ligne, ou colonne.

Voici par exemple à partir de la grille de jeu donnée au format demandé dans le fichier exemples/sudoku.txt :

```bash
$ python3 sudoku.py exemples/sudoku.txt
[6, 3, 8, 7, 1, 2, 9, 4, 5]
[9, 7, 4, 5, 6, 0, 3, 8, 1]
[0, 5, 1, 9, 8, 4, 2, 7, 6]
[8, 1, 6, 2, 9, 5, 4, 3, 7]
[5, 4, 2, 8, 3, 7, 6, 1, 9]
[3, 9, 7, 6, 4, 1, 5, 2, 8]
[7, 8, 9, 4, 2, 0, 1, 6, 3]
[1, 2, 5, 3, 7, 6, 8, 9, 4]
[4, 6, 3, 1, 0, 8, 7, 5, 2]
```

## Utilisation

Lancement de toutes les commandes

```bash
$ make
```

Ainsi tous les résultats sont dans le dossier output/

Sinon voici un exemple d'utilisation :

GSM :

```bash
$ make gsm in=exemples/gsm.txt out=output/gsm_output.txt
```

ou 

```bash
$ python3 gsm.py -i exemples/gsm.txt -o output/gsm_output.txt
```

MAP :

```bash
$ make map in=exemples/map.txt out=output/map_output.txt
```

ou 

```bash
$ python3 map.py -i exemples/map.txt -o output/map_output.txt
```

SUDOKU :

```bash
$ make sudoku
```

ou 

```bash
$ python3 sudoku exemples/sudoku.txt > output/sudoku_output.txt
```

```bash
$ python3 sudoku exemples/sudoku.txt
```
