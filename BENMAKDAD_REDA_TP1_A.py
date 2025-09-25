import random

# je vais utiliser la meme fonction 'echanger' pour tout les exercies


def echanger(tab, i, j):
    tab[i], tab[j] = tab[j], tab[i]


######## EXERCICE 1 ##############
print("########## EXERCICE 1 : #################")


def parition_ex1(tab, i, j):
    indice_pivot = i
    if (i < j):
        for n in range(i+1, j):
            if tab[n] < tab[indice_pivot]:
                i += 1
                echanger(tab, i, n)
        echanger(tab, i, indice_pivot)
    return i


def tri_rapide_ex1(tab, deb, fin):
    if (fin > deb):
        pivot = parition_ex1(tab, deb, fin)
        tri_rapide_ex1(tab, deb, pivot)
        tri_rapide_ex1(tab, pivot+1, fin)


lst = [5, 2, 6, 8, 7, -100, 12, 0, -3, 4, 5]
print("LISTE NON TRIEE : ", lst)
tri_rapide_ex1(lst, 0, len(lst))
print("LISTE TRIEE APRES L'EXECUTION DE L'ALGO DE TRI RAPIDE: ", lst)

######## EXERCICE 2 ##############
print("\n########## EXERCICE 2 : #################")


def parition_ex2(tab, i, j):
    indice_pivot = i
    if (i < j):
        for n in range(i+1, j):
            if tab[n] < tab[indice_pivot]:
                i += 1
                echanger(tab, i, n)
        echanger(tab, i, indice_pivot)
    return i


def tri_rapide_ex2(tab, deb, fin):
    if (fin > deb):
        pivot = parition_ex2(tab, deb, fin)
        etapes_partition = fin - deb + 1
        etapes_gauche = tri_rapide_ex2(tab, deb, pivot)
        etapes_droite = tri_rapide_ex2(tab, pivot+1, fin)
        return etapes_partition + etapes_gauche + etapes_droite
    else:
        return 0


print("POUR LISTES DE 100 ELEMENTS EXERCICE 2 : ")

liste_triee = list(range(0, 100))
nbr_etapes_liste_triee = tri_rapide_ex2(liste_triee, 0, len(liste_triee))
print(f"nombre d'etapes LISTE TRIEE : {nbr_etapes_liste_triee}\n")


liste_inversee = list(range(100, 0, -1))
nbr_etapes_liste_inversee = tri_rapide_ex2(
    liste_inversee, 0, len(liste_inversee))
print(f"nombre d'etapes LISTE INVERSEE : {nbr_etapes_liste_inversee}\n")


liste_aleatoire = []
for i in range(0, 100):
    liste_aleatoire.append(random.randint(0, 1000))

nbr_etapes_liste_aleatoire = tri_rapide_ex2(
    liste_aleatoire, 0, len(liste_aleatoire))
print(f" nombre d'etapes LISTE ALEATOIRE : {nbr_etapes_liste_aleatoire}")


######## EXERCICE 3 ##############
print("\n########## EXERCICE 3 : #################")


def parition_ex3(tab, i, j):
    pos = random.randint(i, j-1)
    echanger(tab, i, pos)
    indice_pivot = i
    if (i < j):
        for n in range(i+1, j):
            if tab[n] < tab[indice_pivot]:
                i += 1
                echanger(tab, i, n)
        echanger(tab, i, indice_pivot)
    return i


def tri_rapide_ex3(tab, deb, fin):
    if (fin > deb):
        pivot = parition_ex3(tab, deb, fin)
        etapes_partition = fin - deb + 1
        etapes_gauche = tri_rapide_ex3(tab, deb, pivot)
        etapes_droite = tri_rapide_ex3(tab, pivot+1, fin)
        return etapes_partition + etapes_gauche + etapes_droite
    else:
        return 0


print("POUR LISTES DE 100 ELEMENTS EXERCICE 3 : ")

liste_triee3 = list(range(0, 100))
nbr_etapes_liste_triee3 = tri_rapide_ex3(liste_triee3, 0, len(liste_triee3))
print(f"nombre d'etapes LISTE TRIEE : {nbr_etapes_liste_triee3}\n")


liste_inversee3 = list(range(100, 0, -1))
nbr_etapes_liste_inversee3 = tri_rapide_ex3(
    liste_inversee3, 0, len(liste_inversee3))
print(f"nombre d'etapes LISTE INVERSEE : {nbr_etapes_liste_inversee3}\n")


liste_aleatoire3 = []
for i in range(0, 100):
    liste_aleatoire3.append(random.randint(0, 1000))

nbr_etapes_liste_aleatoire3 = tri_rapide_ex3(
    liste_aleatoire3, 0, len(liste_aleatoire3))
print(f" nombre d'etapes LISTE ALEATOIRE : {nbr_etapes_liste_aleatoire3}")


######## EXERCICE 4 ##############
print("\n########## EXERCICE 4 : #################")


def parition_ex4(tab, i, j):
    pos_mediane = i + (j - i - 1) // 2
    echanger(tab, i, pos_mediane)
    indice_pivot = i
    if (i < j):
        for n in range(i+1, j):
            if tab[n] < tab[indice_pivot]:
                i += 1
                echanger(tab, i, n)
        echanger(tab, i, indice_pivot)
    return i


def tri_rapide_ex4(tab, deb, fin):
    if (fin > deb):
        pivot = parition_ex4(tab, deb, fin)
        etapes_partition = fin - deb + 1
        etapes_gauche = tri_rapide_ex4(tab, deb, pivot)
        etapes_droite = tri_rapide_ex4(tab, pivot+1, fin)
        return etapes_partition + etapes_gauche + etapes_droite
    else:
        return 0


print("POUR LISTES DE 100 ELEMENTS EXERCICE 4 : ")

liste_triee4 = list(range(0, 100))
nbr_etapes_liste_triee4 = tri_rapide_ex4(liste_triee4, 0, len(liste_triee4))
print(f"nombre d'etapes LISTE TRIEE : {nbr_etapes_liste_triee4}\n")


liste_inversee4 = list(range(100, 0, -1))
nbr_etapes_liste_inversee4 = tri_rapide_ex4(
    liste_inversee4, 0, len(liste_inversee4))
print(f"nombre d'etapes LISTE INVERSEE : {nbr_etapes_liste_inversee4}\n")


liste_aleatoire4 = []
for i in range(0, 100):
    liste_aleatoire4.append(random.randint(0, 1000))

nbr_etapes_liste_aleatoire4 = tri_rapide_ex4(
    liste_aleatoire4, 0, len(liste_aleatoire4))
print(f" nombre d'etapes LISTE ALEATOIRE : {nbr_etapes_liste_aleatoire4}")
