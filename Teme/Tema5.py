
1.

x = int(input('Introdu primul numar: '))
y = int(input('Introdu al doilea numar: '))


def suma_numere(x, y):
    suma = x + y
    return (f'Suma celor doau numere este: {suma}')


print(suma_numere(x, y))



def suma_numere(a, b):
    suma = a + b
    return (f'Suma celor doau numere este: {suma}')


print(suma_numere(8, 10))
print(suma_numere(78, 10))

2.


def par_impar(numar):  # definim functia si ii punem parametrul numar
    if numar % 2 == 0:  # verificam prin modulo daca este par
        return True
    else:
        return False


print(par_impar(84))
print(par_impar(75))

3.



def total_caractere(nume, prenume1, prenume2):
    return len(nume + prenume1 + prenume2)


print(total_caractere('Popescu', 'George', 'Dan'))

4.


def aria_dreptunghi(lungime, latime):
    aria = lungime * latime
    return aria


print(aria_dreptunghi(8, 5))
print(aria_dreptunghi(10, 45))

5.


def aria_cercului(raza):
    aria = raza * raza * 3.14
    return aria


print(aria_cercului(6))
print(aria_cercului(10))

6.


def cautare_caracter(string, x):
    if x in string:
        return True
    else:
        return False


print(cautare_caracter('abc', 'a'))
print(cautare_caracter('abc', 'd'))

7.


def lower_upper(string):
    char_upper = 0
    char_lower = 0
    for char in string:
        if char.isupper():
            char_upper = char_upper + 1
        elif char.islower():
            char_lower = char_lower + 1
    print(f'Numarul de caractere mari este: {char_upper}')
    print(f'Numarul de caractere mici este: {char_lower}')


lower_upper('abc1ABCD!')

8.

lista_numere = [1, -4, 78, -5, 0, 85, 4, -10, -2]


def numere_pozitive(numere):
    lista_numere_pozitive = []
    for numar in numere:
        if numar > 0:
            lista_numere_pozitive.append(numar)
    return lista_numere_pozitive


print(numere_pozitive(lista_numere))

9.


def doua_numere(x, y):
    if x == y:
        print(f'Numerele sunt egale')
    elif x > y:
        print(f'Primul numar {x} este mai mare decat al doilea nr {y}')
    else:
        print(f'Al doilea nr {y} este mai mare decat primul nr {x}')


doua_numere(89, -5)
doua_numere(7, 46)

'''10. 

set_numere_input = {2, 5, 8, 78, -8, 45}
set_numere_input = {2, 5, 8, 78, -8, 45}


def adaugare_numar(set_numere, numar_nou):
    if numar_nou in set_numere:
        print(f'nu am adaugat numarul {numar_nou} in set, exista deja')
        return False
    else:
        set_numere.add(numar_nou)
        print(f'am adaugat numarul {numar_nou} in set')
        return True


print(adaugare_numar(set_numere_input, 78))
print(adaugare_numar(set_numere_input, 75))


11. 


def calendar(luna):
    lunile_anului = {
        'January': 31,
        'February': 28,
        'March': 31,
        'April': 30,
        'May': 31,
        'June': 30,
        'July': 31,
        'August': 31,
        'September': 30,
        'October': 31,
        'November': 30,
        'December': 31
    }
    if luna in lunile_anului:
        return lunile_anului.get(luna)


print(calendar('June'))
print(calendar('January'))
print(calendar('February'))


12.



def calculator(x, y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return a, b, c, d


a, b, c, d = calculator(3, 2)

print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)

14. 


def maxim(x, y, z):
    if x == y == z:
        return ('numerele sunt egale')
    elif x >= y and x >= z:
        return (f'{x} este cel mai mare numar')
    elif y >= x and y >= z:
        return (f'{y} este cel mai mare numar')
    else:
        return (f'{z} este cel mai mare numar')


print(maxim(20, 20, 2))
print(maxim(5, 100, 100))
print(maxim(7, 7, 7))
print(maxim(17, 2, 17))


13. 
lista1 = [1, 1, 2, 7, 7, 7]


def count(lista):
    cnt = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0
    }
    for i in cnt.keys():
        for j in lista:
            if i == j:
                cnt[i] = cnt[i] + 1
    return cnt


print(count(lista1))


14. 


def maxim(a, b, c):
    if a == b and b == c:
        max = a
    elif a >= b and a >= c:
        max = a
    elif b >= a and b >= c:
        max = b
    else:
        max = c
    return max


print(maxim(5, 7, 2))  # returneaza 7
print(maxim(7, 6, 2))  # returneaza 7
print(maxim(5, 6, 7))  # returneaza 7
print(maxim(4, 4, 4))  # returneaza 4
print(maxim(4, 3, 3))  # returneaza 4
print(maxim(3, 4, 3))  # returneaza 4
print(maxim(3, 3, 4))  # returneaza 4


15. 


def suma_num(a):
    suma = 0
    for i in range(0, a + 1):
        suma = suma + i
    return suma


print(suma_num(3))  # returneaza 6


16. 

list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]


def common_nr(l1, l2):
    set1 = set(l1)
    set2 = set(l2)
    return set1.intersection(set2)


print(common_nr(list1, list2))


17. 


def reducere_preturi(price, sale):
    if sale > 100 or sale < 0:
        return 'reducere invalida'
    new_price = price - (sale / 100) * price
    return new_price


print(reducere_preturi(100, 10))  # 90
print(reducere_preturi(100, -1))  # no
print(reducere_preturi(100, 101))  # no

'''
18.
'''
from datetime import datetime


def data_ora():
    date_time = datetime.now()
    dt_string = date_time.strftime("%d/%m/%Y %H:%M:%S")
    print("Date and Time: ", dt_string)


data_ora()

# 19. 
from datetime import date


def amr_xmas(year):
    christmas_day = date(year=year, month=12, day=25)
    days_til_christmas = (christmas_day - date.today()).days
    return days_til_christmas


print(amr_xmas(2022))