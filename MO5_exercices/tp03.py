import random

ECOSYSTEM_SIZE = 3

SPECIE_1 = 1
SPECIE_2 = 2
SPECIE_3 = 3

def intialize_ecosystem() -> list:
    """
    Permet d'initialiser un écosystème
    :return: Une matrice 3*3 simulant un écosystème
    """
    # ecosystem = list() # Autre syntaxe possible
    ecosystem = []

    for line_index in range(ECOSYSTEM_SIZE):
        line = []
        for column_index in range(ECOSYSTEM_SIZE):
            line.append(random.randint(SPECIE_1, SPECIE_3))
        ecosystem.append(line)

    return ecosystem

def display_ecosystem(ecosystem: list) -> None:
    """
    Affiche un écosystème passé en paramètre
    :param ecosystem:
    :return:
    """
    for line_index in range(len(ecosystem)):
        for column_index in range(len(ecosystem[line_index])):
            print(ecosystem[line_index][column_index], " ", end="")
        print("", end="\n") # Passe à la ligne

def update_ecosystem(ecosystem: list) -> list:

    species_count = {
        SPECIE_1: 0,
        SPECIE_2: 0,
        SPECIE_3: 0,
    }

    target_specie = ecosystem[1][1]
    predator_specie = 0

    if target_specie == SPECIE_1:
        predator_specie = SPECIE_3
    elif target_specie == SPECIE_2:
        predator_specie = SPECIE_1
    else:
        predator_specie = SPECIE_2

    count_target_specie = 0
    count_predator_specie = 0

    # On compte les espèces cibles et prédateurs
    for line_index in range(len(ecosystem)):
        for column_index in range(len(ecosystem[line_index])):
            # Condition sera à supprimer pour faire des tests à la fin
            if line_index != 1 or column_index != 1:
                if ecosystem[line_index][column_index] == predator_specie:
                    count_predator_specie += 1
                elif ecosystem[line_index][column_index] == target_specie:
                    count_target_specie += 1

    if count_predator_specie > count_target_specie:
        ecosystem[1][1] = predator_specie
    elif count_predator_specie == count_target_specie:
        ecosystem[1][1] = random.choice([predator_specie, target_specie])

    return ecosystem

ecosystem = intialize_ecosystem()
display_ecosystem(ecosystem)
print(80*"-")
ecosystem = update_ecosystem(ecosystem)
display_ecosystem(ecosystem)
print(80*"-")