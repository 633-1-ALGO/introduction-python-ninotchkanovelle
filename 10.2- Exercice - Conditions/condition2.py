# Problème : Déterminer si une année est bissextile ou non. Pour cela, il faut avoir ces règles en tête :
#                   Si une année n'est pas multiple de 4, on s'arrête là, elle n'est pas bissextile.
#                   Si elle est multiple de 4, on regarde si elle est multiple de 100.
#                       Si c'est le cas, on regarde si elle est multiple de 400.
#                           Si c'est le cas, l'année est bissextile.
#                           Sinon, elle n'est pas bissextile.
#                       Sinon, elle est bissextile.
#
# Résultat attendu : Un message affichant "Année bissextile" ou "Année non bissextile"

a = 2000
mult = 4

somme = a%4

multcent = a%100
multquatrecent = a%400


if somme > 0:
    print("Année non bissextile")
elif multcent > 0 and multquatrecent > 0:
    print("Année non bissextile")
else:
    print("Année bissextile")



