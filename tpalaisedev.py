"""
____________ EXO 1 ____________
str = input('Enter a string: ')

print(str[::-1])

if str[::-1] == str:
    print("C'est un palindrome")
else: print("Ce n'est un palindrome")

____________ EXO 2 ____________

voyelle = ["a", "e", "i", "o", "u", "y"]
nb_voyelle=0
nb_consonne=0
str = input('Enter a string: ')
for i in range(len(str)):
    if str[i] in voyelle:
        nb_voyelle+=1
    else: nb_consonne+=1

print(nb_voyelle)
print(nb_consonne)

____________ EXO 3 ____________ """
story = """
Ce matin-là, Jules était déjà en retard. 
Il saute dans sa vieille voiture, tourne la clé... rien. 
Putain, pas aujourd’hui.
Il sort, claque la portière un peu trop fort. 
Il tente de bricoler sous le capot, comme s’il savait ce qu’il faisait. 
Bien sûr, aucune idée. Il se coupe un doigt. Merde, évidemment.
Il finit par appeler son pote Karim, qui lui répond encore à moitié endormi :
— Putain, t’as encore oublié de faire la vidange ou quoi ?
Jules rigole nerveusement. 
Le genre de rire qui veut dire "je vais exploser". 
Finalement, Karim arrive, le dépanne tant bien que mal. 
Jules monte enfin dans la voiture de secours, en route pour une journée qui s’annonce… longue."""

mots_interdits = "merde putain crotte"
mot_int = mots_interdits.split()
for i in range(len(mot_int)):
    mot_int[i] = mot_int[i].capitalize()
print(mot_int)
test = story.strip(",.")

for i in range(len(test)):
    test[i].strip(',')
    if test[i] in mot_int:
         print(test[i])
         del test[i]



