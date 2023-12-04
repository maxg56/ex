def present(tableau, cible):
    """Indique par True ou False si cible est un élément de tableau"""
    for elt in tableau:
        if elt == cible:
            return True
    return False


def compte(tableau, cible):
    """Compte le nombre d'occurence de cible dans tableau"""
    total = 0
    for elt in tableau:
        if elt == cible:
            total += 1
    return total


def premiere_occurence(tableau, cible):
    """Renvoie l'indice de la première occurrence de cible dans tableau

    Si cible n'est pas présent, on renvoie la taille du tableau
    """
    for i in range(len(tableau)):
        if tableau[i] == cible:
            return i
    return len(tableau)


def derniere_occurence(tableau, cible):
    """Renvoie l'indice de la dernière occurrence de cible dans tableau

    Si cible n'est pas présent, on renvoie la taille du tableau
    """
    for i in range(len(tableau) - 1, -1, -1):
        if tableau[i] == cible:
            return i
    return len(tableau)


def maximum(tableau):
    """Renvoie la valeur du maximum du tableau

    Si le tableau est vide on renvoie 0
    """
    if tableau == []:
        return 0

    maxi = tableau[0]
    for i in range(1, len(tableau)):
        if tableau[i] > maxi:
            maxi = tableau[i]

    return maxi


def minimum(tableau):
    """Renvoie la valeur du minimum du tableau

    Si le tableau est vide on renvoie None
    """
    if tableau == []:
        return None

    mini = tableau[0]
    for i in range(1, len(tableau)):
        if tableau[i] < mini:
            mini = tableau[i]

    return mini


def ecarts(tableau):
    """Renvoie le tableau composé des écarts abs(tableau[i] - tableau[i + 1])

    On garantit que tableau compte au moins deux valeurs
    """
    return [abs(tableau[i] - tableau[i + 1]) for i in range(len(tableau) - 1)]


def moyenne(notes):
    """Calcule la moyenne des notes contenues dans le tableau

    notes est un tableau non vide

    Toutes les notes sont sur 20, coefficient 1

    La moyenne est arrondie au centième en faisant round(moyenne, 2)
    """
    if notes ==[]:
        raise ValueError("")
    somme = 0
    for une_note in notes:
        somme += une_note

    return round(somme / len(notes), 2)


def moyennes_classe(classe):
    """Calcule la moyenne des élèves de la classe

    classe est un dictionnaire {"nom de l'élève": tableau de notes}

    Chaque tableau de notes est non vide. Toutes les notes sont sur 20, coefficient 1

    Renvoie un nouveau dictionnaire au format {"nom de l'élève": moyenne} dans lequel les
    moyennes sont arrondies au centième
    """
    resultat = dict()

    for eleve in classe:
        resultat[eleve] = moyenne(classe[eleve])

    return resultat
