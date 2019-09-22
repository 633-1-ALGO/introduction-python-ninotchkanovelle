# Consigne : Récupérer le mot "chaine" du string s et l'afficher
s = 'un exemple de chaine'
i = 0 # On appelle l'indice 'i' par convention
while i < len(s):
    if s[i]=="c":
        print(s[i]+s[i+1]+s[i+2]+s[i+3]+s[i+4]+s[i+5])
    #print(s[i]) # On affiche le caractère à chaque tour de boucle
    i += 1
