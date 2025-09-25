from BENMAKDAD_REDA_TP1_B_QGEN import trirapide_gen



class Personne:
    def __init__(self, nom, age, salaire):
        self.nom = nom
        self.age = age
        self.salaire = salaire


    def affiche(self):
        print(f"Je m'appelle {self.nom}, j'ai {self.age} ans, et j'ai un salaire mensuel de {self.salaire} euros")


print("#### Tri personnes par age croissant : ###")
def compare_age_croissant(personneA, personneB):
    return personneA.age < personneB.age

liste_personnes = [Personne('A', 22, 10000), Personne('B', 19, 700), Personne('C', 15, 500), Personne('D', 30, 15000), 
                   Personne('E', 45, 5000), Personne('F', 12, 0), Personne('G', 55, 2500), Personne('H', 21, 9000),
                   Personne('I', 90, 1200), Personne('G', 80, 1500), Personne('K', 20, 300), Personne('L', 44, 6000) ]

for personne in liste_personnes:
    personne.affiche()


print("\n#### Tri personnes par salaire decroissant : ###")
def compare_salaire_decroissant(personneA, personneB):
    return personneA.salaire > personneB.salaire

trirapide_gen(liste_personnes, 0, len(liste_personnes), compare_salaire_decroissant)

for personne in liste_personnes:
    personne.affiche()