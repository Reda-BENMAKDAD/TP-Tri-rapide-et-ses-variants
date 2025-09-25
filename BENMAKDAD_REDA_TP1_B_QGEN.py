def echanger(tab, i, j):
    tab[i], tab[j] = tab[j], tab[i]


def parition_ex1(tab, i, j, compare):
    indice_pivot = i
    if (i < j):
        for n in range(i+1, j):
            if compare(tab[n], tab[indice_pivot]):
                i += 1
                echanger(tab, i, n)
        echanger(tab, i, indice_pivot)
    return i


def trirapide_gen(tab, deb, fin, compare):
    if (fin > deb):
        pivot = parition_ex1(tab, deb, fin, compare)
        trirapide_gen(tab, deb, pivot, compare)
        trirapide_gen(tab, pivot+1, fin, compare)



