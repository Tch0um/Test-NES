from math import *

def test():
    valeur = input("Selectionnez un entier de départ: ")
    valeur=valeur[::-1]                                  #On retourne le nombre renseigné afin de faciliter son traitement
    for i in range(0,len(valeur)-1):                     #Boucle au travers la liste des premier chiffre a comparer
        for j in range(i+1,len(valeur)):                 #Boucle au travers la liste des seconds chiffre a comparer
            if valeur[i]>valeur[j]:                      #Comparaison des deux chiffres                                       
