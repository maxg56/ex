import corriges_1
from random import randrange, choice
from functools import reduce
from string import ascii_lowercase


def present(tableau, cible):
    """Indique par True ou False si cible est un élément de tableau"""
    for i in tableau :
        if i == cible:
            return True
    return False

def compte(tableau, cible):
    """Compte le nombre d'occurence de cible dans tableau"""
    nombre_cible = 0
    if present(tableau,cible)==False:
        return nombre_cible 
    for i in tableau :
        if i == cible:
            nombre_cible +=1
            
    return nombre_cible


def premiere_occurence(tableau, cible):
    """Renvoie l'indice de la première occurrence de cible dans tableau

    Si cible n'est pas présent, on renvoie la taille du tableau
    """
    indice_cible = 0
    if present(tableau,cible)==False:
        return len(tableau)
    for i in range(len(tableau)) :
        if tableau[i] == cible:
            indice_cible = i
            
    return indice_cible 


def derniere_occurence(tableau, cible):
    """Renvoie l'indice de la dernière occurrence de cible dans tableau

    Si cible n'est pas présent, on renvoie la taille du tableau
    """
    indice_cible = 0
    if present(tableau,cible)==False:
        return len(tableau)
    for i in range(len(tableau)) :
        if tableau[i] == cible:
            indice_cible = i
            
    return indice_cible 


def maximum(tableau):
    """Renvoie la valeur du maximum du tableau

    Si le tableau est vide on renvoie 0
    """
    maxi= tableau[0]
    for i in tableau:
        if  i > maxi:
            maxi = i
    return maxi


def minimum(tableau):
    """Renvoie la valeur du minimum du tableau

    Si le tableau est vide on renvoie None
    """
    if tableau == []:
        return None
    mini= tableau[0]
    for i in tableau:
        if  i < mini:
            mini = i

    return mini


def ecarts(tableau):
    """Renvoie le tableau composé des écarts abs(tableau[i] - tableau[i + 1])

    On garantit que tableau compte au moins deux valeurs
    """
    tableau_ecarts=[None for i in range(len(tableau-1))]
    for i in range(len(tableau-1)):
        tableau_ecarts.append(abs(tableau[i] - tableau[i + 1]))  
    return tableau_ecarts


def moyenne(notes):
    """Calcule la moyenne des notes contenues dans le tableau

    notes est un tableau non vide

    Toutes les notes sont sur 20, coefficient 1

    La moyenne est arrondie au centième en faisant round(moyenne, 2)
    """
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




#######################################
#                TESTS                #
#######################################

# Préparatifs
taille = 30
mini = -50
maxi = 50
tableau = [randrange(mini, maxi) for _ in range(taille)]
cible_presente = choice(tableau)
cible_absente = choice([mini - 1, maxi + 1])

notes = [randrange(0, 21) for _ in range(10)]

nombre_eleves = 10
classe = dict()
for _ in range(nombre_eleves):
    prenom = "".join([choice(ascii_lowercase) for _ in range(6)])
    nombre_notes = randrange(1, 10)
    classe[prenom] = [randrange(0, 21) for _ in range(nombre_notes)]


# Décommenter chaque bloc successivement afin de tester les fonctions indépendamment

print(f"{tableau = }")
print(f"{cible_presente = }")
print(f"{cible_absente = }")

# present
assert present(tableau, cible_presente) is True
assert present(tableau, cible_absente) is False

# comtpe
assert compte(tableau, cible_presente) == tableau.count(cible_presente)
assert compte(tableau, cible_absente) == 0

# première occurrence
#
assert premiere_occurence(tableau, cible_presente) == tableau.index(cible_presente)
assert premiere_occurence(tableau, cible_absente) == taille

# dernière occurrence
assert derniere_occurence(tableau, cible_presente) == corriges_1.derniere_occurence(tableau, cible_presente)
assert derniere_occurence(tableau, cible_absente) == taille

# maximum
assert maximum(tableau) == reduce(lambda x, y: x if x > y else y, tableau, mini)

# minimum
assert minimum(tableau) == reduce(lambda x, y: x if x < y else y, tableau, maxi)

# écarts
#assert ecarts(tableau) == corriges_1.ecarts(tableau)

# écarts
#tableau[0]assert ecarts(tableau) == corriges_1.ecarts(tableau)

print(f"{notes = }")
print(f"{classe = }")

# moyenne
assert moyenne(notes) == corriges_1.moyenne(notes)

# moyenne de la classe
assert moyennes_classe(classe) == corriges_1.moyennes_classe(classe)
