eleves = [
    "Karim Benali", "Ines Dubois", "Adrien Lefèvre", "Sofia Haddad", "Mehdi Bensalem", "Clara Moreau", "Julien Marchand",
    "Amira Zeroual", "Lucas Petit", "Sarah Khelifi", "Nicolas Durand", "Leïla Bouzid", "Thomas Lambert", "Amina Taleb",
    "Hugo Fontaine", "Lina Merabet", "Yassine El Moudden", "Emma Lemoine", "Maxime Garcia", "Nawel Aït Ali", "Romain Girard",
    "Chloé Bernard", "Antoine Masson", "Samira Bekkali", "Bastien Roche", "Lila Benyahia", "Quentin Noël", "Jade Amrani",
    "Yanis Saidi", "Camille Robert", "Alexandre Fabre", "Hana Moumen", "Théo Muller", "Myriam Djemai", "Enzo Caron",
    "Salma Charef", "Victor Perrin", "Zoé Rahmani", "Ayoub Sebbar", "Manon Tessier"
]

# utilise map pour renvoyer créer une liste avec seulement les prénoms
# utilise map pour remplacer ï par i, é par e, è par e

first_name = list(map(lambda p:  p.rsplit(' ', 1)[0], eleves))
replace_letter = list(map(lambda p:  p.replace("ï", "i").replace("é", "e").replace("è", "e"), eleves))

print(first_name)
print(replace_letter)