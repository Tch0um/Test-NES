from math import *

def checkout(shoplist):
    total=0
    for i in range(0,len(shoplist)):
        if (shoplist[i].lower()) in ["pomme","0"]:
            total+=0.60
        if (shoplist[i].lower()) in ["orange","1"]:
            total+=1.25
    print(total,"$")
    return total

