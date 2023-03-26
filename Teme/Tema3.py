

# 1.

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
#a
print(note_muzicale)
#b
note_muzicale = note_muzicale[::-1]
print(note_muzicale)
#c
note_muzicale.reverse()
print(note_muzicale)

#2
print(note_muzicale.count('do'))

#3
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
lista_noua = lista1 + lista2
print(f"Lista unita cu varianta 1 este: {lista_noua}")

lista1.extend(lista2)
print(f"Lista unita cu varianta 2 este: {lista1}")

#4
lista_noua_v1.sort()
print(f"Lista sortata este: {lista_noua_v1}")
lista_noua_v1.remove(0)
print(f"Lista sortata dupa stergerea numarului 0 este: {lista_noua_v1}")

#5
# Lista este goala (IF)
# Lista nu este goala (ELSE)
if len(lista_noua_v1) >= 1:
    print('Lista nu este goala')
else:
    print('Lista este goala')

#6
lista_noua_v1.clear()

#7
if len(lista_noua_v1) >= 1:
    print('Lista nu este goala')
else:
    print('Lista este goala')

#8
dict1 = {
    'Ana': 8,
    'Gigel': 10,
    'Dorel': 5}
print(dict1.keys())

#9
print(f'Ana a luat nota: {dict1["Ana"]}')
print(f'Gigel a luat nota: {dict1["Gigel"]}')
print(f'Gigel a luat nota: {dict1.get("Dorel")}')

#10
dict1['Dorel'] = 6
print(dict1.get('Dorel'))

#11
dict1.pop('Gigel')
print(f"Dictionarul dupa transferul ul lui Gigel: {dict1}")
dict1['Ionica'] = 9
print(f"Dictionarul dupa transferul ul lui Ionica: {dict1}")


#12

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(f"Lista a ramas identica pentru ca nu se pot afisa duplicate: {zile_sapt}")

#13
if weekend.issubset(zile_sapt):
    print('weekend este un subset al zilelor sapt')
else:
    print('weekend NU este un subset al zilelor sapt')

#14
diferenta1 = zile_sapt.difference(weekend)
diferenta2 = weekend.difference(zile_sapt)
print(f"Diferenta dintre zile_sapt si weekend este: {diferenta1}")
print(f"Diferenta dintre weekend si zile_sapt este: {diferenta1}")

#15
intersectia = zile_sapt.intersection(weekend)
print(f"Intersectia dintre cele doua seturi este: {intersectia}")




#1

SCHIMBARI_MAXIME = 3
schimbari_efectuate = 2

schimbari_ramase = SCHIMBARI_MAXIME - schimbari_efectuate
lista_jucatori_teren = ['j1', 'j2', 'j3', 'j4', 'j5']
lista_jucatori_rezerva = ['j6','j7','j8','j9','j10']
lista_jucatori_scosi = []
jucator_in = 'j6'
jucator_out = 'j1'


if jucator_out in lista_jucatori_teren and schimbari_ramase > 0:
    if jucator_in in lista_jucatori_rezerva and jucator_in not in lista_jucatori_teren: # eliminam cazul cand jucatorul este deja in teren
        lista_jucatori_teren.remove(jucator_out)  # scoatem jucatorul
        lista_jucatori_scosi.append(jucator_out)
        lista_jucatori_teren.add(jucator_in)  # adaugam jucatorul nou
        lista_jucatori_rezerva.remove(jucator_out)
        schimbari_ramase = schimbari_ramase - 1  # contorizam schimbarea
        print(f'Schimbare efectuata cu succes!')
        print(f'A intrat {jucator_in}, a iesit {jucator_out}, mai aveti {schimbari_ramase} schimbari')
else:
    if schimbari_ramase <= 0:
        print('Nu mai ai schimbari')
    else:
        print(f'Nu se poate efectua schimbarea deoarece jucatorul {jucator_out} nu e in teren')
print(f'Actuala echipa este {echipa}')
print(f"Jucatorii care au fost scosi sunt: {lista_jucatori_scosi}")