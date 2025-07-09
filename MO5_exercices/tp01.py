import re
import string

txt = input('Enter a string: ')

intab = "àéïoù"
outtab = "aeiou"
trantab = str.maketrans(intab, outtab)

res = txt.translate(trantab).lower().replace(" ", "")

print(res)


if res[::-1] == res:
    print(f"C'est un palindrome{res}")
else:print(f"Ce n'est pas un palindrome {res}")
