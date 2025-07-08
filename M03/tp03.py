def display_chessboard():
    total_rice = 0
    grain_rice = 1

    for lines in range(8):
        for column in range(8):
            print(f"Case [{lines + 1}, {column + 1}] : {grain_rice} grains de riz")
            total_rice += grain_rice
            grain_rice *= 2
    print("\nTotal des grains de riz sur l'échiquier :", total_rice)

display_chessboard()
