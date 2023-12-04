def dicho(tableau, cible):
    """
    Recherche la cible dans le tableau à l'aide de la recherche dichotomique

    Voir https://nreveret.forge.aeif.fr/preuves_visuelles/#recherche-dichotomique

    tableau est non vide et trié dans l'ordre croissant

    Renvoie l'indice de cible dans tableau si cible est présent,
    la longueur du tableau sinon
    """
    gauche = 0
    droite = len(tableau) - 1
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if tableau[milieu] > cible:
            droite = milieu - 1
        elif tableau[milieu] < cible:
            gauche = milieu + 1
        else:
            return milieu

    return len(tableau)


def minimum_depuis(tableau, indice):
    """
    Renvoie l'indice du minimum du tableau à partir de l'indice fourni

    tableau est non-vide
    indice est un indice compris entre 0 et len(tableau) - 1

    Si le minimum apparaît plusieurs fois, on renvoie l'indice de sa première occurrence

    Par exemple minimum_depuis([3, 8, 2, 9, 3, 10], 0) renvoie 0
    alors que minimum_depuis([3, 8, 2, 9, 3, 10], 1) renvoie 3
    """
    mini = tableau[indice]
    i_maxi = indice
    for i in range(indice + 1, len(tableau)):
        if tableau[i] < mini:
            mini = tableau[i]
            i_maxi = i
    return i_maxi


def tri_selection(tableau):
    """
    Trie tableau en utilisant le tri par sélection

    tableau est non-vide

    Le tri est en place : tableau est directement modifié
    La fonction ne renvoie rien
    """
    for i in range(len(tableau) - 1):
        i_maxi = minimum_depuis(tableau, i)
        tableau[i], tableau[i_maxi] = tableau[i_maxi], tableau[i]


def tri_insertion(tableau):
    """
    Trie tableau en utilisant le tri par insertion

    tableau est non-vide

    Le tri est en place : tableau est directement modifié
    La fonction ne renvoie rien
    """
    for i in range(1, len(tableau)):
        a_inserer = tableau[i]
        j = i
        while j > 0 and tableau[j - 1] > a_inserer:
            tableau[j] = tableau[j - 1]
            j -= 1
        tableau[j] = a_inserer
