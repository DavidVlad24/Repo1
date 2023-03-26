
# Ex:1

"""
daca conditie = True
    se executa acest bloc de cod
altfel
    se executa acest bloc de cod
"""


# Ex:2
x = 3
if x >= 0 and type(x==int):
    print(f"{x} este un numar natural.")
else:
    print(f"{x} nu este un numar natural.")

# Ex:3

x = 5
if x > 0:
    print('Numarul este pozitiv')
elif x < 0:
    print('Numarul este negativ')
else:
    print('Numarul este neutru')

# Ex:4

x = 3
if x >= -2 and x <= 13:
    print('Acest numar este curpins intre -2 si 13. ')
else:  # aceasta cerinta nu era specificata in exercitiu
    print('Acest numar nu este cuprins intre -2 si 13')

# Ex:5
x = 13
y = 8
if x - y < 5:
    print('Diferenta este mai mica decat 5.')
else:
    print('Diferenta nu este mai mica decat 5')

# Ex:6
x = 4
if not (5 <= x <= 27):
    print('Numarul nu este intre 5 si 27.')

# Ex:7
x = 9
y = 9
if x == y:
    print("Numerele x si y sunt egale.")
elif x > y:
    print(f"{x} este valoarea lui x si este mai mare decat y.")
else:
    print(f"{y} este valoarea lui y si este mai mare decat x.")

# Ex:8
x = 4
y = 4
z = 4
if (x == y and x != z) or (x == z and x != y) or (y == z and y != x):
    print('Triunghiul este isoscel.')
elif x == y == z:
    print('Triunghiul este echilateral.')
else:
    print('Triunghiul este oarecare.')

# Ex:9 -
letter = input('Introduceti o litera: ')
letter = letter.lower()
if letter.isdigit():
    print('Nu ai introdus o litera, ci altceva.')
elif letter.upper() == 'a' or letter.upper() == 'e' or letter.upper() == 'i' or letter.upper() == 'o' or letter.upper() == 'u':
    print('Litera este vocala.')
else:
    print('Litera nu este vocala.')



nota = float(input("Care este nota primita? "))
if 9 < nota <= 10:
    nota = "A"
    print(f"Nota primita in sistemul american este {nota}")
elif nota >= 8:
    nota = "B"
    print(f"Nota primita in sistemul american este {nota}")
elif nota >= 7:
    nota = "C"
    print(f"Nota primita in sistemul american este {nota}")
elif nota >= 6:
    nota = "D"
    print(f"Nota primita in sistemul american este {nota}")
elif nota > 4:
    nota = "E"
    print(f"Nota primita in sistemul american este {nota}")
elif 4 >= nota >= 0:
    nota = "F"
    print(f"Nota primita este {nota}")
else:
    print('Nu a-ti introdus o nota de la 0 la 10.')




# Ex:1
x = -999
if 999 < x or x>=10000:
    print('nu are 4 cifre')
else:
    print('are 4 cifre')

# Ex:2
x = 125645
if len(str(x)) == 6:
    print('are 6 cifre')
else:
    print('nu are 6 cifre')

# Ex:3
x = 44
if x % 2 == 0:
    print("Numarul este par.")
else:
    print("Numarul este impar.")

# # Ex:4
x = 4
y = 4
z = 2
if x >= y and x >= z:
    print(f'{x} este cel mai mare numar')
elif y >= x and y >= z:
    print(f'{y} este cel mai mare numar')
else:
    print(f'{z} este cel mai mare numar')

# Ex:5
x = 5
y = 8
z = 3
if x + y + z == 180 and x > 0 and y > 0 and z > 0:
    print('Triunghiul este valid.')
else:
    print('Triunghiul nu este valid.')

# Ex:16

string = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('Alege cate caractere vrei sa tai de la final'))
print(string[0:-x])

# Ex:17

string = 'Coral is either the stupidest animal or the smartest rock'
string1 = string[0:5]
string2 = string[-5:]
print(f'{string1}{string2}')

# Ex


string = 'Coral is either the stupidest animal or the smartest rock'
index_rock = string.index('rock')
print(string[:index_rock])

# Ex:9
word = input('alege un str')
assert word[0].lower() == word[len(word)-1].lower(), 'Primul si ultimul caracter sunt diferite'

# Ex:
word = '0123456789'
print(word[0::2])
print(word[1::2])

"""
Exerciții Bonus 
"""

# 1.

varsta = int(input("Va rugam sa introduceti varsta pasagerului "))
pasaport_valid = input("E pasaportul valid? Da/Nu ")
if varsta>=18 and pasaport_valid == "Da":
    print("Va puteti imbarca")
elif varsta<18 and pasaport_valid == "Da":
    ambii_parinti = input("E copilul insotit de ambii parinti? ")
    if ambii_parinti == "Da":
        print("Va puteti imbarca")
    else:
        permisiune = input("Permisiune parinte lipsa: ")
        if permisiune == "Da":
            print("Va puteti imbarca")
        else:
            print("Nu va puteti imbarca")
else:
    print("Nu va puteti imbarca")



# 2. Joc de noroc



import random
dice_roll = random.randint(0, 6)
guess = int(input('Ghiceste zarul'))
if guess < dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {guess} dar a fost {dice_roll}')
elif guess > dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {guess} dar a fost {dice_roll}')
else:
    print(f'Ai ghicit. Felicitari! Ai ales {guess} si zarul a fost {dice_roll}')
