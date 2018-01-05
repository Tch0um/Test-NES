from math import *

def checkout(shoplist):
    total=0
    for i in range(0,len(shoplist)): #boucle de parcours de la liste prise en entrée
        if (shoplist[i].lower()) in ["pomme","0"]: #détection des pommes 
            total+=0.60
        if (shoplist[i].lower()) in ["orange","1"]: #détection des oranges
            total+=1.25
    print(total,"$") #affichage du total
    return total

# modifier la liste ci dessous pour changer le shopping cart
# "pomme" ou "0" pour une pomme , "orange" ou "1" pour une orange 
checkout(["Orange","1","PoMmE","0"])
