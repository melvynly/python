def nombre_de_Conway(un_nombre=1):
    suivante = []
    ligne = list(str(un_nombre))
    chiffre_actuel = ligne[0]
    compteur = 0
    for chiffre in ligne:
        if chiffre == chiffre_actuel:
            compteur += 1
        else:
            suivante.append(str(compteur))
            suivante.append(chiffre_actuel)
            chiffre_actuel = chiffre
            compteur = 1
    suivante.append(str(compteur))
    suivante.append(chiffre_actuel)
    return int("".join(suivante))

PROFONDEUR = 15

nombre = 1
for i in range(PROFONDEUR):
    print("{0:03}. {1}".format(i+1, nombre))
    nombre = nombre_de_Conway(nombre)
