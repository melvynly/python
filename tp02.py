x = int(input("Entrer un numéro de chèque : "))
total_amount = 0
most_200 = {"amount":0, "number":0}
less_200 = {"amount":0, "number":0}

def display_stat(total_amount, number_cheque, most_200, less_200):
    print(f"Montant total : {total_amount}")
    print(f"Nombre de cheque introduit : {number_cheque}")
    print(f"Moyenne des montants : {total_amount / number_cheque}")
    print(f"Nombre de cheques dont le montant "
          f"est inferieur a 200€ {less_200['number']} "
          f"et le montant total de {less_200['amount']}")
    print(f"Nombre de cheques dont le montant "
          f"est inferieur a 200€ {most_200['number']} "
          f"et le montant total de {most_200['amount']}")

while x != 0:
    number_cheque = 1
    print(x)
    amount = float(input("Entrer le montant : "))
    total_amount += amount
    number_cheque += 1

    if amount > 200:
        most_200["amount"] += amount
        most_200["number"] += 1

    elif amount < 200:
        most_200["amount"] += amount
        most_200["number"] += 1

    x = int(input("Entrer un numéro de chèque : "))

    if x == 0:
        display_stat(total_amount, number_cheque, less_200, most_200)
        break
