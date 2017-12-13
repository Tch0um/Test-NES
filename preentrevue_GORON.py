from math import *



def test():
    valeur = input("Selectionnez un entier de départ: ")
    valeur=valeur[::-1]                                  #On retourne le nombre renseigné afin de faciliter son traitement
    for i in range(0,len(valeur)-1):                     #Boucle au travers la liste des premier chiffre a comparer
        for j in range(i+1,len(valeur)):                 #Boucle au travers la liste des seconds chiffre a comparer
            if valeur[i]>valeur[j]:                      #Comparaison des deux chiffres
                tamplist=list(valeur)                    #Transformation de la de la valeur en liste afin d'effectuer les échanges de valeur
                tamp=tamplist[j]                         #  ---
                tamplist[j]=tamplist[i]                  # Échange des deux valeurs
                tamplist[i]=tamp                         #  ---
                tamplist=tamplist[::-1]                  #On retourne la liste dans le bon ordre avant de l'afficher
                print(tamplist,"\n")
                return tamplist
    return("aucune valeur superieure avec les chiffres renseignés ") #Cas ou l'on a atteint la valeur maximale avec les chiffres renseignés
                      
        

