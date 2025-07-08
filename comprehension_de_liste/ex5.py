# crée une liste de liste
# pour les tables de multiplications de 1 à 10
# [[1,2,3,...], [2,4,6,...],...]

liste = []

for i in range(1, 11):
    liste.append((i,i))
    for j in range(1, 11):
        lises = []
        print(i*j)
        liste.append(lises)

print(liste)




