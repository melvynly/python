#soit la liste d'élèves suivante
eleves = [
    "Thomas", "Bertrand", "Marie", "Etienne", "Jean", "Arnaud", "Bertrand", "Xavier", "Martin", "Jeanne",
    "David", "Rodolphe", "Genevieve", "Pierre", "Karim", "Ines", "Adrien", "Magalie", "Romaric", "Antoine",
    "Karim", "Ines", "Adrien", "Sofia", "Mehdi", "Clara", "Julien", "Amira", "Lucas", "Sarah", "Nicolas",
    "Leïla", "Thomas", "Amina", "Hugo", "Lina", "Yassine", "Emma", "Maxime", "Nawel", "Romain", "Chloé",
    "Antoine", "Samira", "Bastien", "Lila", "Quentin", "Jade", "Yanis", "Camille", "Alexandre", "Hana",
    "Théo", "Myriam", "Enzo", "Salma", "Victor", "Zoé", "Ayoub", "Manon"
]

# compte le nombre d'élèves
# en utilisant filter, crée un liste avec les élèves dont le prénom contient un a
# en utilisant filter, crée un liste avec les élèves dont le prénom contient plus de 7 caractère
# en utilisant filter, crée un liste avec les élèves dont le prénom fini par un d

with_a = list(filter(lambda  p: "a" in p, eleves))
most_7_charactere = list(filter(lambda p: len(p) > 7 , eleves))
last_d = list(filter(lambda p: p[-1] == "d", eleves))

print(with_a)
print(most_7_charactere)
print(last_d)