"""Fonction n°1(Max)
Écrire une première fonction prenant deux valeurs numériques en paramètre
et qui retourne la plus grande des deux.

Fonction n°2 (Compare)
Écrire une seconde fonction prenant également deux valeurs numériques
en paramètre mais qui retourne une des valeurs suivantes
• 0 : si les deux valeurs sont égales
• 1 : si la première valeur est la plus grande
• -1 : sinon (la seconde valeur est la plus

Fonction n°3 (Test de Max et Compare)
À partir de valeurs à saisir, écrire une fonction
permettant de tester les deux précédentes"""

#Fonction 1
def most_value(a, b):
    return a if a > a else b

def most_value_return(value_1, value_2):
    return 1 if value_1 > value_2 else 0 if value_1 > value_2 else -1

#print(most_value_return(2, 2))

def test_most_value_return(value_1, value_2):
    print(most_value(value_1, value_2))
    print(most_value_return(value_1, value_2))

print(test_most_value_return(4, 2))



