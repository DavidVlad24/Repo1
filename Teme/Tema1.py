
#Ex_1 
"""
O variabila o adresa de memorie in care putem sa stocam informatii. Ele pot fi de mai multe feluri: Intregi, sir de caractere, boolean, float
"""
#Ex_2
# string
# int
# float

tara = "Danemarca" 		#variabila de tip string
nr = 1 								#variabila de tip int
numar = 1.8 					#variabila de tip float
y = True						  #variabila de tip bool

#Ex_3
print(type(tara))
print(type(nr))
print(type(numar))
print(type(y))

#Ex_4

numar_rotunjit = round(numar)
print(numar_rotunjit)
print(type(numar_rotunjit))

#Ex_5
nume = "Ioana"
numar_ani = 2.5
zile_ramase = 30
numar_ore = 4
print(f"{nume} s-a mutat in Spania de {y} ani.")
print(f"{nume} este mai mare ca sora ei cu {numar_ani} ani. ")
print(f"{zile_ramase} zile mai sunt pana {nume} merge in vacanta. ")
print(f"{nume} lucreaza doar {numar_ore} ore pe zi.")

#Ex_6
nume = input('Numele este: ')
prenumele = input('Prenumele este: ')
print(f'Numele complet are {len(nume) + len(prenumele)} caractere')

#Ex_7
lungimea = int(input('Lungimea dreptunghiului este: '))
latimea = int(input('Latimea dreptunghiului este: '))
print(f'Aria dreptunghiului este {lungimea * latimea} metri patrati.')

#Ex_8
prop ='Coral is either the stupidest animal or the smartest rock'
print(prop.count(' the '))

#EX_9
prop ='Coral is either the stupidest animal or the smartest rock'
print(f'{prop.replace("the", "THE")}')

#Ex_10
prop ='Coral is either the stupidest animal or the smartest rock'
#


#Ex_1
text = str(input('Scrie un string: '))
print(f'Caracterul din mijloc este: {text[(len(text)//2)]}')

#Ex_2
text = 'ana'
assert text == text[::-1], 'Cuvantul nu este palindrom'

#Ex_3

text = input('Scrie un string: ')
x, y = text.split(' ')
print(f'Primul cuvant este: {x}')
print(f'Ultimul cuvant este: {y}')

#Ex_14
# salvează primul caracter într-o variabilă
# capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.
text = str(input('Scrie un string: '))
prima_litera = text[0]
string_modificat = text[0]+text[1:len(text)-1].replace(x,x.upper())+text[len(text)-1]
print(string_modificat)

#Ex_15
user = str(input('User-ul este: '))
parola = str(input('Tasteaza parola: '))
parola_ascunsa = '*' * len(parola)
print(f'Parola pentru userul {user} este {parola_ascunsa} si are {len(parola)} caractere')