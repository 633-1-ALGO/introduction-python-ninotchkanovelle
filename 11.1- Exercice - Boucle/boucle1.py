# Problème : Etant donné un tableau A de "n" nombres réels, on demande la moyenne des nombres du tableau
# Données : un tableau A de n nombre réels
# Résultat attendu : Moyenne des nombres réels du tableau A
A = [1, 5, 15, 25, 10, 55, 50, 35]
moy: float = 0 # resultat
n: int = len(A)  # taille du tableau
i: int = 0

while i < n:
    moy += A[i]/n
    i = i + 1

moy += moy / n

print(moy)
