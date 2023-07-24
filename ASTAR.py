"""
    PTOJET RP (Qst 4 ( A star) en utilisant pygame)
    - LABCHRI Amayas
    - KOULAL Yidhir Aghiles

    Master 1 IV
"""

from tkinter import *
from tkinter import messagebox
import sys, threading
import pygame
import numpy as np
from time import sleep

sys.setrecursionlimit(10 ** 7)
threading.stack_size(2 ** 27)

#Fonction d'initialisation
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_HEIGHT = 300
WINDOW_WIDTH = 300

# Matrices du taquin

#Matrice correcte (Ou on veut y arriver)
matrice = np.array([
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5],
])
#Matrice S (Ou on commence)
mat = np.array([
     [2,8,3],
     [1,6,4],
     [7,0,5],
    ])


# le main
def main():
    # on declare deux variables globales pour facilites les modifications
    global SCREEN, CLOCK
    pygame.init()  # on initilise une fenetre pygame
    pygame.display.list_modes()

    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)  # le background en blanc
    # fonction pour dessiner la grille a partir de la matrice
    drawGrid()
    c = True
    while c:
        pygame.display.update()  # mettre a jour le jeu
        c = a_star(mat, 0, False)
        pygame.display.update()  # on effectue les modifications


# fonction qui dessine la grille
def drawGrid():
    blockSize = 100  # distance entre chaque case de la grille

    for x in range(0, WINDOW_WIDTH, blockSize):

        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)  # creer un rectangle
            pygame.draw.rect(SCREEN, BLACK, rect, 1)  # dessiner un rectangle dans la matrice (grille)


# fonction qui remplit la grille avec des nombres
def Nombre(matrice):
    sleep(1)

    i = 0
    j = 0
    # font est arial avec une taille de 30
    font = pygame.font.SysFont("arial", 30)
    for x in range(0, WINDOW_HEIGHT, 100):
        for y in range(0, WINDOW_WIDTH, 100):

            # si la valeur de la case est differente de 0 on ne dessine rien dans la case
            if matrice[j, i] != 0:
                text = font.render(str(matrice[j, i]), False, BLACK)  # le text est la valeur de la matrice
                SCREEN.blit(text, (x + 50, y + 50))  # on met le text dans la position (x+50, y+50)

            j = j + 1
        i = i + 1
        j = 0  # des avoir fini une ligne de la matrice on remet l indice des colonnes a 0


# fonction qui retourne la postion (x,y) de la case vide dans la matrice
def rechercher_vide(matrice_img):
    librei=0
    librej=0
    for i in range(3):
        for j in range(3):
            if (matrice_img[i][j] == 0):
                librei = i
                librej = j
                break

    return (librei, librej)


# Fonction qui compare 2 matrice (Condition d'arret) si S est equivalante a la matrice correcte
def comparerMat(mat1, mat2):
    eg = True
    for i in range(mat1.shape[0]):
        for j in range(mat1.shape[1]):
            if (mat1[i][j] != mat2[i][j]):
                eg = False
    return eg

# Fonction qui calcul l'heuristique(Nombre de cases qui sont pas dans leurs propre place)
def h(mat, matrice_img):
    x = 0
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if (mat[i][j] != matrice_img[i][j] and mat[i][j] != 0):
                x = x + 1
    return x

# Algorithme A star
def a_star(mat, g, term):
    nbrcoups = ""
    SCREEN.fill(WHITE)
    drawGrid()
    Nombre(mat)
    pygame.display.update()
    # term est une variable boolean qu'on donne en entrée a notre fonction(initialement term=faux)
    if (term == True):
        #Si term est vrai alors On a pu arriver a la matrice juste et tous les nombres sont dans leurs places
        print("\n\n\nL'algorithme est fini , vous avez gagné dans le jeu de TAQUIN")
        SCREEN.fill(WHITE)
        drawGrid()
        Nombre(mat)
        pygame.display.update()
        nbrcoups = "Vous avez ganger avec un nombre de coups = " + str(g)
        Tk().wm_withdraw()  # to hide the main window
        messagebox.showinfo('Felicitation', nbrcoups)
        c = False

        return c
    else:#Si term est faux
        #On commence par comparer les 2 matrices
        reussir = comparerMat(mat, matrice)
        print("reussir = ", reussir)
        #Si les deux matrices sont identiques
        if (reussir == True):
            #On appelle A star avec (term=vrai) pour arreter le processus avec succes
            a_star(mat, g, True)

        else:#Si les deux matrices sont differentes
            #ON initialise les 4 matrices(Au max on a 4 deplacements)
            mat1 = np.copy(mat)
            mat2 = np.copy(mat)
            mat3 = np.copy(mat)
            mat4 = np.copy(mat)
            #on incremente le gain(le pas)
            g = g + 1
            f1 = f2 = f3 = f4 = 1000
            print("\n\n \nmatrice initiale\n")
            #on cherche la position de la case vide
            ilibre, jlibre = rechercher_vide(mat)
            n = mat.shape[0]
            #on modifie les matrices pour chaque deplacement possible
            if (ilibre != n - 1):
                z = mat1[ilibre + 1][jlibre]
                mat1[ilibre + 1][jlibre] = 0
                mat1[ilibre][jlibre] = z
                # afficher(mat1)
                SCREEN.fill(WHITE)
                drawGrid()
                Nombre(mat1)
                pygame.display.update()
                h1 = h(mat1, matrice)
                f1 = g + h1
                print("h1 = ", h1)
                print("g = ", g)
                print("f1 = ", f1)

            SCREEN.fill(WHITE)
            drawGrid()
            Nombre(mat)
            pygame.display.update()
            if (jlibre != n - 1):
                z = mat1[ilibre][jlibre + 1]
                mat2[ilibre][jlibre + 1] = 0
                mat2[ilibre][jlibre] = z
                print("mat2")
                # afficher(mat2)
                SCREEN.fill(WHITE)
                drawGrid()
                Nombre(mat2)
                pygame.display.update()
                h2 = h(mat2, matrice)
                f2 = g + h2
                print("h2 = ", h2)
                print("g = ", g)
                print("f2 = ", g + h2)

            SCREEN.fill(WHITE)
            drawGrid()
            Nombre(mat)
            pygame.display.update()
            if (ilibre != 0):
                z = mat1[ilibre - 1][jlibre]
                mat3[ilibre - 1][jlibre] = 0
                mat3[ilibre][jlibre] = z
                print("mat3")
                # afficher(mat3)
                SCREEN.fill(WHITE)
                drawGrid()
                Nombre(mat3)
                pygame.display.update()
                h3 = h(mat3, matrice)
                f3 = g + h3
                print("h3 = ", h3)
                print("g = ", g)
                print("f3 = ", g + h3)

            SCREEN.fill(WHITE)
            drawGrid()
            Nombre(mat)
            pygame.display.update()
            if (jlibre != 0):
                z = mat1[ilibre][jlibre - 1]
                mat4[ilibre][jlibre - 1] = 0
                mat4[ilibre][jlibre] = z
                print("mat4")
                # afficher(mat4)
                SCREEN.fill(WHITE)
                drawGrid()
                Nombre(mat4)
                pygame.display.update()
                h4 = h(mat4, matrice)
                f4 = g + h4
                print("h4 = ", h4)
                print("g = ", g)
                print("f4 = ", g + h4)

            SCREEN.fill(WHITE)
            drawGrid()
            Nombre(mat)
            pygame.display.update()
            # Chercher la composition qui a comme nombres de cases invalides minimal
            min = f1
            if (f2 < min):
                min = f2
            if (f3 < min):
                min = f3
            if (f4 < min):
                min = f4
            print("Min des f = ", min)
            en = False
            #On appelle A star (recursivite) avec la nouvelle matrice(qui a F minimale)
            if (f1 == min and reussir == False and en == False):
                en = True
                a_star(mat1, g, reussir)
            if (f2 == min and reussir == False and en == False):
                en = True
                a_star(mat2, g, reussir)
            if (f3 == min and reussir == False and en == False):
                en = True
                a_star(mat3, g, reussir)
            if (f4 == min and reussir == False and en == False):
                en = True
                a_star(mat4, g, reussir)


main()
