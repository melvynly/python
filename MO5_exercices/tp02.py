test = list(input("Rentrez la phrase : "))
test1 = list(input("Rentrez la phrase 1 : "))

def compta_letter(word):
    dict_letters = {}
    for letter in word:
        if letter not in dict_letters:
            dict_letters[letter] = 1
        else:
            dict_letters[letter] += 1
    return dict_letters

if compta_letter(test) == compta_letter(test1):
    print("C'est un anagramme")
else: print("Ce n'est pas un anagramme")
