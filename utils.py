def calcul_nb_voisins(Z):
    forme = len(Z), len(Z[0])
    N = [[0, ] * (forme[0]) for i in range(forme[1])]
    for x in range(1, forme[0] - 1):
        for y in range(1, forme[1] - 1):
            N[x][y] = Z[x-1][y-1]+Z[x][y-1]+Z[x+1][y-1] \
             + Z[x-1][y] + 0+Z[x+1][y] \
            + Z[x-1][y+1]+Z[x][y+1]+Z[x+1][y+1]
    return N
def iteration_jeu(Z):
    forme = len(Z), len(Z[0])
    N = calcul_nb_voisins(Z)
    for x in range(1,forme[0]-1):
        for y in range(1,forme[1]-1):
            if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
                Z[x][y] = 0
            elif Z[x][y] == 0 and N[x][y] == 3:
                Z[x][y] = 1
    return Z
import matplotlib.pyplot as plt
def iterations(Z):
    plt.subplots(figsize=(15,8))
    for i in range(10):
        ax = plt.subplot(2,5,i+1)
        plt.imshow(Z, extent=[0,len(Z[0]),0,len(Z)])
        plt.grid(True)
        ax.set_xticks(range(0,len(Z[0]),1))
        plt.title('Itération ' + str(i))
        
        Z = iteration_jeu(Z) 
        

    plt.show()
    def calcul_nb_voisins_np(Z):
    T= np.zeros_like(Z)
    for i in range(1, Z.shape[0]-1):
        for j in range(1, Z.shape[1]-1):
            T[i,j]+=Z[i,j-1]+Z[i,j+1]+Z[i-1,j-1]+Z[i-1,j]+Z[i-1,j+1]+Z[i+1,j-1]+Z[i+1,j]+Z[i+1,j+1]
    return T
            def iteration_jeu_np(Z):
    # on affecte la matrice qui calcule le nombre de voisins à N.
    N=calcul_nb_voisins_np(Z)
    for i in range(1, Z.shape[0]-1):
        for j in range(1, Z.shape[1]-1):
            #Donne True si au moins un élément  est vrai. Faux est aussi donné dans le cas où c'est vide.
            # toute cellule vivante avec 2 ou 3 voisins vivants reste  vivante à la génération suivante, donc toute cellule vivante qui n'a pas 2 ou 3 voisins vivants devient morte.
            if (Z[i,j].any==1) and (N.any != 2 and N.any != 3):
                Z[i,j]=0
                # toute cellule morte ayant exactement 3 voisins vivants devient une cellule vivante.
            elif Z[i,j].any==0 and N.any == 3:
                Z[i,j]=1
    return Z
def jeu_np(Z_in, nb_iter):
    Z_apres=np.array(Z_in)
    for i in range (nb_iter):
        Z_apres=iteration_jeu(Z_in)
    return Z_apres
Z_in = np.array([[0,0,0,0,0,0],[0,0,0,1,0,0],[0,1,0,1,0,0],[0,0,1,1,0,0],[0,0,0,0,0,0], [0,0,0,0,0,0] ])
A=jeu_np(Z_in, 1)
print("La matrice Z_in après la première itération est : {}" .format(A))
B=jeu_np(Z_in,2)
print("La matrice Z_in après la deiscième itération est : {}" .format(B))
