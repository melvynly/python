def calcul_temps_cuisson(poids, cuisson, viande):
    temps_ref = {
        "Boeuf": {
            "Bleu": 10,
            "À Point": 17,
            "Bien Cuit": 25
        },
        "Porc": {
            "Bleu": 15,
            "À Point": 25,
            "Bien Cuit": 40
        },
        "Canard": {
            "Bleu": 20,
            "À Point": 25,
            "Bien Cuit": 30
        }

    }

    temps_pour_500g = temps_ref[viande].get(cuisson)
    temps_final = (poids / 500) * temps_pour_500g
    return round(temps_final, 2)


def main():
    print("Calcul du temps de cuisson.")
    viande = input("Entrez le poids de la viande en grammes (Boeuf, Porc, Canard) : ")
    poids = float(input("Entrez le poids de la viande en grammes : "))
    cuisson = input("Entrez le mode de cuisson (Bleu, À Point, Bien Cuit) : ")
    resultat = calcul_temps_cuisson(poids, cuisson, viande)
    print(f"Temps de cuisson estimé : {resultat} minutes.")


if __name__ == "__main__":
    main()
