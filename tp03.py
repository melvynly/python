PRIX_CAFE = 0.6
piece_accepte = [2, 1, 0.5, 0.2, 0.1, 0.05]
solde = 0


while solde < PRIX_CAFE:
    piece = float(input("Entrez la valeur de la pièce : "))
    if piece in piece_accepte:
        solde += piece
    else : print("Piece non accepte")
    print(solde)
    if solde > PRIX_CAFE:
        print("Voici votre cafe")
        break



