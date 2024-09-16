"""
jqehnze
"""
#### Fonction secondaire


def ispalindrome(p):
    """
    determine si le mot est un palyndrome
    argument: chaine de caractere s
    return: True si palyndrome, False sinon
    """
    table = str.maketrans(
    "áàâäãåéèêëíìîïóòôöõúùûüýÿñçÁÀÂÄÃÅÉÈÊËÍÌÎÏÓÒÔÖÕÚÙÛÜÝÑÇ,-'?!:",
    "aaaaaaeeeeiiiiooooouuuuyyncAAAAAAEEEEIIIIOOOOOUUUUYNC      "
    )
    p=p.lower() # regler le pb des majuscules
    p=p.translate(table)#regle le pb des accents
    a=0
    b=-1
    rg=0 #variable pour faire le moins d'iteration possible sur p
    if len(p)%2==0: #si pair on met la moitié du mot en iteration
        rg=len(p)//2
    else:
        rg=len(p)//2+1 #si impair, la moitié +1 pour le caractere du milieu
    for i in range(rg):
        #print(f"test numero {i}:{p[a]}!={p[b]}",a,b) #pour observer chaque iteration
        if p[a]!=p[b]: # si different
            if p[a]==" ":         # si different car espace 
                while p[a]==" ":  # saute tous les espaces
                    a+=1
                    #print(f"p[a]={p[a]}")
            elif p[b]==" ":
                while p[b]==" ":  #pareil saute espaces
                    b-=1
                    #print(f"p[b]={p[b]}")
            elif p[a]!=p[b]:
                return False
            else:  # si pas different a cause des espaces
                #print(f"{p[a]}!={p[b]}",a,b)
                return False
        a+=1
        b-=1
    return True

#### Fonction principale


def main():
    """
    teste la fonction pour voir si elle fonctionne dans la plupart des cas
    """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie","azerreza"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
