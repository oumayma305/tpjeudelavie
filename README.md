# tpjeudelavie
Le jeu de la vie se présente sous la forme d'un univers à deux dimensions (une grille). chaque cellule occupe une zone délimitée de cet univers (une case).

Cet espace n'est pas continu mais vous pourrez trouver certains automates celullaires dont les bords se touches - l'univers prend alors la forme d'un tore (donuts) - .

En plus de cette univers à 2 dimension, nous ajoutons la dimension du temps. Celui-ci est découpé en pulsations. A chaque pulsation, le programe calcule la nouvelle configuration des cellules dans l'univers.

Chaque cellule est régie par trois règles simples :

Une cellule morte entourée d'exactement trois cellules vivantes naît.
Une cellule vivante entourée de deux ou trois cellules vivantes reste en vie
Dans les autres cas, la cellule meure.
