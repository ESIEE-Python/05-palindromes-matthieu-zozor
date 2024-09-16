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
    p=p.replace(" ","")
    rg=0 #variable pour faire le moins d'iteration possible sur p
    if len(p)%2==0: #si pair on met la moitié du mot en iteration
        rg=len(p)//2
    else:
        rg=len(p)//2+1 #si impair, la moitié +1 pour le caractere du milieu

    for i in range(rg):
        #print(f"test numero {i}:{p[i]}!={p[-i-1]}",i,-i-1) #pour observer chaque iteration
        if p[i]!=p[-i-1]:
            return False
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
