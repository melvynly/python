# crée une liste de liste
# pour les tables de multiplications de 1 à 10
# [[1,2,3,...], [2,4,6,...],...]

# Plus elegant mais pas possible de debugger
liste = [[i*j for j in range(1, 11)] for i in range(1, 11)]

for i in range(1, 11):
    table = []
    for j in range(1, 11):
        table.append(i * j)
    liste.append(table)

print(liste)