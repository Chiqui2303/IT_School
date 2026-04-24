import turtle
# Functii in Python - o functie este un bloc de cod


# sintaxa
# def nume_functie(parametru1, parametru2,.....),
# def salut(nume):
#     print(f"Salut,{nume}")
#
# salut("Sorin")
#
# def adunare(a,b):
#     return a+b
# rezultat = adunare(3,5)
# print(rezultat)

# functii fara parametri sau return
#
# def afiseaza_mesaj():
#     print("Functie fara parametri")
#
# afiseaza_mesaj()

# paarmetri impliciti
#
# def salut(nume="user"):
#     print(f"salut {nume}")
# salut()
# salut("Sorin")

# # domenii de vizibilitatate

 # variabile:
# 1. globale - in afara functiilor
# 2. locale - in interiorul functiilor
# 3. enclosing - functii nested (imbricate)
# 4. built-in - functii/variabile predefinite
#
# x=10
# def test():
#     x=5
#     print("Local",x)
# test()
#
# print("Global:",x)
#
# modificare variabila globala dintr-o functie

# x=10
# def modificat():
#     global x
#     x=20
#
# print(x)
# modificat()
# print(x)


# scope enclosing(functii nested/imbricate)

# def functie_exterioara():
#     mesaj="exterior"
#     def functie_interioara():
#         print(mesaj)
#     functie_interioara()
# functie_exterioara()

# Functii lambda (functii anonime)

# suma=lambda a,b:a+b
#
# print(suma(3, 4))

# enclosing scope (nonlocal)

# def exterior():
#     x=10
#     def interior():
#         nonlocal x
#         print(x)
#         x+=1
#         print(x)
#     interior()
# exterior()

# LEGB - python cauta variabilele in urmatoare ordine
# 1. Local
# 2. Enclosing
# 3. Global
# 4. Built-in

# Exemplu LEGB

# x="Global"
#
# def functia_exterioara():
#     x="enclosing"
#     def functia_interioara():
#         x="local"
#         print("in functia interioara",x)
#     functia_interioara()
#     print("in functia exterioara",x)
# functia_exterioara()
# print("in afara functiilor",x)


# Exercitii:
# o functie care gaseste cel mai mare numar

# def cel_mai_mare_nr(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
# a=int(input("introduceti primul nr:"))
# b=int(input("introduceti primul nr:"))
# c=int(input("introduceti primul nr:"))
# rezultat=cel_mai_mare_nr(a,b,c)
# print(f"Cel mai mare numar este: {rezultat}.")

# # o functie care verifica nr par
# def este_par(numar):
#      return numar % 2 == 0
#
# print("este 4 par?: ", este_par(4))
# print("este 5 par?: ", este_par(5))

# numaratoare inversa
# def countdown(n):
#     while n >= 0:
#         print(n)
#         n -= 1
# countdown(10)

# instructiunea return

# functie care returneaza o valoare
# def suma(a, b):
#     suma = a + b
#     return suma
# rezultat = suma(1, 2)
# print(rezultat)

# return cand opreste functia

# def functie():
#     print("inainte de return")
#     return
#     print("dupa return")
# functie()

# fara return explicit - None
# def salut():
#     print("Salut")
# x = salut()
# print(x)

# return poate afisa valori multiple
# def test():
#     return 3, 5
# x, y = test()
# print(y, x)

# modalitate            # ce returneaza
# 1. return valoare     # 1. intoarce "valoare"
# 2. return             # 2. intoarce None
# 3. nicio instructiune # 3. intoarce None
# 4. return x, y, z     # 4. intoarce tuplu(x, y, z)

# Util ca sa separi logica functiei de restul codului

# desenam un patrat/dreptunghi
# def patrat():
#     for i in range(4):
#         turtle.forward(100)
#         turtle.right(90)
# turtle.speed(10)
# patrat()
# turtle.done()

# exercitiu - calculator salariu
# def calculeaza_salariu_net(salariu_brut):
#     impozit=salariu_brut*0.10
#     CAS=salariu_brut*0.25
#     salariu_net=salariu_brut-impozit-CAS
#     return salariu_net
#
# def afiseaza_fluturas(salariu_brut):
#     impozit = salariu_brut * 0.10
#     cas = salariu_brut * 0.25
#     salariu_net = calculeaza_salariu_net(salariu_brut)
#
#     print("Fluturas salariu")
#     print("Salariu brut: ", salariu_brut)
#     print("impozit 10%: ", impozit)
#     print("cas 25%: ", cas)
#     print("salariu net: ", salariu_net)

# brut = float(input("Introdu salariul brut: "))
# afiseaza_fluturas(brut)


numar_conversii = 0

def conversie_temperatura():
    # enclosing scope
    unitate = "celsius"

    celsius = float(input("Introdu temperatura in grade Celsius: "))

    def calculeaza():
        # local scope
        f = celsius * 9 / 5 + 32
        k = celsius + 273.15

        print(f"\nTemperatura introdusa: {celsius} {unitate}")
        print(f"Fahrenheit: {f}")
        print(f"Kelvin: {k}")

        global numar_conversii
        numar_conversii += 1
    calculeaza()
conversie_temperatura()
conversie_temperatura()

print(f"nr conversii efectuate: {numar_conversii}")