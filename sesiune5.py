# Conditionale - if/elif/else
# o conditie este o expresie care poate fi adevarata(True) sau falsa(False).
# pe baza ei, putem decide daca anumite blocuri de cod se vor executa sau nu

# if conditie:
#     # codul se executa doar daca conditia este True
# elif alta_conditie:
#     # codul se executa daca prima conditie nu a fost True, dar aceasta este
# else:
#     # codul se executa daca niciuna dintre conditii nu a fost adevarata/indeplinita

#exemplu:
varsta = 11

if varsta >= 18:
    print("Ai voie sa votezi")
else:
    print("esti prea tanar ca sa votezi")

# Python foloseste indentare pentru a sti ce cod apartine blocului if/else etc. Nu folosim acolade {} ca in alte limbaje
x = 11
if x > 10:
    print("Mai mare")
print("Final")

# Operatori de comparatie

# 1. == -> egal cu
# a = 5
# b = 3
# a == b -> False

# 2. != -> diferit de
# a != b -> True

# 3. > -> mai mare decat
# a > b -> True

# 4. < -> mai mic decat
# a < b -> False

# 5. >= -> mai mare sau egal
# a >= b -. True

# 6. <= -> mai mic sau egal
# a <= b -> False

# 1. Egal cu - ==
x=5
if x==5:
    print("x este egal cu 5")

# 2. Diferit de - !=
if x != 10:
     print("x NU este egal cu 10")

# 3. Mai mare decat - >
temperatura=30
if temperatura>25:
    print("Afara e cald")

# 4. Mai mic decat - <
elevi=18
if elevi <19:
    print("Clasa este mica")

# 5. Mai mare sau egal
varsta = 18
if varsta >= 18:
    print("Ai voie sa votezi")

# 6. Mai mic sau egal
pret = 99
if pret <= 99:
    print("Produsul este ieftin")

# Operatori logici

# 1. AND -> ambele conditii trebuie sa fie True / Adevarate
# 2. OR -> cel putin una din conditii trebuie sa fie True
# 3. NOT -> inverseaza valoarea - True -> False


# 1. AND
varsta = 19
nationalitate = "roman"

if varsta > 18 and nationalitate == "roman":
    print("Poti vota in Romania")
else:
    print("Nu poti vota in Romania")

# 2. OR
zi = "sambata"
if zi == "sambata" or zi == "duminica":
    print("Este weekend")

# 3. NOT
ploua = False
if not ploua:
    print("Vremea este frumoasa")

# if not x -> aceasta este o verificare de tip "falsy". Python interpreteaza valoarea lui "x" in contextul de adevar sau fals
# if x: verifica daca x este adevarat (Truthy)
# if not x: verifica daca x este fals (Falsy)

# Ce valori sunt considerate falsy in Python
# Toate vor face ca not x sa fie True, adica sa execute codul din interiorul if:
"""
1. None
2. False
3. 0 (orice numar 0)
4. ''/"" -> sir gol
5. [] -> lsita goala
6. {} -> dictionar gol
7. set() -> set gol
8. () -> tuplu gol

5, 6, 7, 8 -> colectii de date
"""
# Exemple concrete
x = 0
print(bool(x))
print(not x)
if not x:
    print("Este zero")

x = ""
if not x:
    print("String gol")

x = [1, 2, 3]
if not x:
    print("Lista este goala") # NU se va afisa, lista contine elemente
else:
    print("Lista are elemente")

# Alte modalitati de a scrie if

# 1. if pe o singura linie
x = 3
if x % 2 != 0: print("Numar impar")

# 2. if ternar(pe o singura linie - inlocuieste if/else)
x = 8
rezultat = "Par" if x % 2 == 0 else "Impar"
print(rezultat)

if x%2==0:
    rezultat="Par"
else:
    rezultat="Impar"
print(rezultat)

# 3. if cu in (verificare apartenenta)
litera = "a"
if litera in "aeiou":
    print("Este vocala")
else:
    print("Este consoana")

# 4. if cu bool() (conditie implicita)
nume = "Maria"
if nume:
    print("Ai introdus un nume")

# 5. if comparativ cu mai multe valori
x = 7
if 5 < x < 10:
    print("x este intre 5 si 10")

# Nested if - if in interiorul altui if - folosit pentru mai multe niveluri de verificare
# varsta =int(input("introdu varsta ta"))
# if varsta>=18:
#     print("Esti adult")
#     if varsta>=65:
#         print("Esti pensionar")
#     else:
#         print("Inca muncesti")
# else:
#     print("Esti minor")

#exercitiu 1
# 1 citeste un mumar de la tastatura si verifica daca e par sau nu
#
# numar=int(input("nr:"))
# if numar%2==0:
#     print("par")
# else:
#     print("impar")

# afiseaza daca un numar este pozitiv negativ sau zero
#
# numar1=int(input("Numarul este: "))
# if numar1 ==0:
#     print("Este zero")
# elif numar1>0:
#     print("Este pozitiv")
# else:
#     print("Este negativ")
#
# verifica daca un nr introdus de la tastatura este intre 1 si 100

# numar=int(input("Numarul este: "))
# if numar>1 and numar <=100:
#     print("Numarul este in interval.")
# else:
#     print("Numarul nu este in interval.")
# #
# if 1<numar<=100:
#     print("Numarul este in interval.")
# else:
#     print("Numarul nu este in interval.")

#A se introduce de la tastatura temperatura si dupa aceea daca este sub 0 este ger intre 0-15 este frig intre 16-25 este placut si pete 25 este cald

temperatura=float(input("Ce temperatura este afara?: "))
if temperatura<0:
    print("Afara este ger.")
    if temperatura<-5:
        print("Posibilitate de ninsoare.")
elif 0<=temperatura<=15:
    print("Afara este frig.")
elif temperatura>15 and temperatura<=25:
    print("Afara este placut.")
else:
    print("Afara este cald.")
print("Sfirsit!")
