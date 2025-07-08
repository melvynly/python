def est_premier(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

nombres_premiers = [n for n in range(2, 1001) if est_premier(n)]
print(nombres_premiers)


limit = input("Quel est la limite ?")