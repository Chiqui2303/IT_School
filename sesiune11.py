# o lista reprezinta o coleectie de date/valori pastrate intr-o anumita ordine
#Exemplu:
# fructe=["mere", "banane", "portocale"]
# print(fructe)

#o lista poate contine
# numere=[1,2,3]
# nume= ["Florin","Mihai", "Andrei"]
# valori_mixte=[10,"florin",True,False,1.2]

#listele sint ordonate
# sint modificabile
# pot contine valori duplicate
#pot contine tipuri de date diferite

# folosim liste atunci cind avem mai multe valori care apartin aceleiasi categorii
# note=[7,6,9,10]
# echipament_it=["laptop","pc","mouse"]
# temperaturi=[21.5,30,17.5]
# persoane=["Ana", "Florin","Bogdan"]

# citeva diferente intre liste, tupluri, seturi si dictionare

#o lista este ordonata si modificabila

#un tuplu in schimb, seamana cu lista dar nu il poti modifica dupa creare

# ex_tuplu=(10,20)
#pastreaza ordinea
#permite duplicate
#nu se poate modifica

# un set este o colectie fara ordine fixa si fara duplicate
#
# ex_set={1,2,3,3,3}
# print(ex_set)
#
# ex_set={1,2,3,3,3,5,7,10,6}
# print(ex_set)

# nu garanteaza ordinea
# nu permite duplicate
# e folosit pentru eliminarea duplicatelor

# un dictionar pastreaza datele sub forma cheie-valoare

# student={
#     "nume": "Florin",
#     "varsta":26,
#     "oras": "Timisoara"
# }
#folosit pentru structurarea datelor
#in dictionar accesezi valorile dupa cheie, nu dupa index numeric

# exemplu
# note=[10,8,9,7]
# print(note)
# print("prima nota din lista:", note[0])
# print("Cite note sint in lista", len(note))

# exercitiu: creeaza o lista cu 5 orase si afiseaza

# lista_orase=["timisoara","cluj","Bucuresti", "Iasi", "Lugoj"]
# print(lista_orase)

# Crearea listelor
# lista=[]

# folosim functia list
# litere=list("Python")
# print(litere)
#
# numere= list(range(1,6))
# print(numere)

# list comprehension
# numere=[1,2,3,4,5]
# nr_dublate=[numar*2 for numar in numere]
# print(nr_dublate)

# patrate=[]
#
# for numar in range(1,6):
#     patrate.append(numar*numar)
# print(patrate)
#
# patrate=[numar*numar for numar in range(1,6)]
# print(patrate)
# [ce adaug in lista for fiecare element in colectie]

# accesare elemente din lista

# index pozitiv
# pozitiile elementelor din o lista se numesc indexuri

# fructe=["mere","banane","portocale"]
# print(fructe[0])
# print(fructe[1])
# print(fructe[2])

# index negativ
# pornim de la finalul listei
# print(fructe[-1])
# print(fructe[-2])
# print(fructe[-3])

# slicing
# sintaxa-> lista[start:stop]
# start este inclus
# stop nu este inclus
#
# numere=[1,2,3,4,5]
# print(numere[1:4])
#
# nume=["Florin", "Maria","Andrei", "Mihai", "Ionut"]
# print(nume[0:3])
# print(nume[2:5])
# print(nume[:3])
# print(nume[2:])
#
# numere=[1,2,3,4,5,6,7]
# print(numere[:3])
# print(numere[4:])
# print(numere[-3:])

# slicing cu pasi
# sintaxa-> lista[start:stop:pas]
# numere=[1,2,3,4,5,6,7]
# print(numere[0:8:2])
# print(numere[::2])
#

# inversarea unei liste cu slicing
# lista_inversata=lista[::-1]
# Exemplu:
#
# numere=[1,2,3,4,5]
# invers=numere[::-1]
# print(invers)

# modificarea listelor
# modificarea prin index
#
# masini=["audi","Logan","BMW"]
# print(masini)
# masini[1]="Mercedes"
# print(masini)

# modificarea prin slicing
# numere=[1,2,3,4,5]
# print(numere)
# numere[1:4]=[20,30,40]
# print(numere)

# modificare prin slicing cu numar diferit de elemente
# numere=[1,2,3,4,5]
# print(numere)
# numere[1:3]=[100,200,300,400]
# print(numere)

# adaugare cu append

# nume=["Florin", "Mihai"]
# print(nume)
# nume.append("Maria")
# print(nume)

# inserare cu insert - adauga un element intr-o anumita pozitie din lista

# fructe=["mere", "pere"]
# print(fructe)
# fructe.insert(1,"banane")
# print(fructe)

# extinderea cu extend - adauga into lista elementele din alta lista
# lista1=[1,2,3]
# lista2=[4,5,6]
# print("lista 1 inainte de extindere", lista1)
# lista1.extend(lista2)
# print("lista 1 dupa de extindere",lista1)
# print(lista2)

# lista=[1,2]
# lista.append([3,4])
# lista.extend([3,4])
# print(lista)

# stergerea elementelor din lista

# del() sterge un element dupa index

# fructe=["mere","pere","banane"]
# del fructe[1]
# print(fructe)

#remove() sterge dupa valoare nu dupa index
# fructe=["mere","pere","banane"]
# fructe.remove("banane")
# print(fructe)
#
# fructe=["mere","pere","pere","banane"]
# fructe.remove("banane")
# print(fructe)

# stergere cu pop - sterge un element si il returneaza. daca nu specifici indexul, sterge ultimul element
# fructe=["mere","pere","banane"]
# ultimul_element=fructe.pop()
# print("Element sters:",ultimul_element)
# print(fructe)

# fructe=["mere","pere","banane"]
# sters=fructe.pop(0)
# print("element sters",sters)
# print(fructe)

# stergere cu clear() - sterge lista complet
# numere=[1,2,3,4]
# print(numere)
# numere.clear()
# print(numere)


# Alte functii utile
# sort() - sorteaza lista

# numere=[2,6,1,7,15,100,1001]
# print(numere)
# numere.sort()
# print(numere)

# reverse() - inverseaza lista originala
#
# numere=[2,6,1,7,15,100,1001]
# print(numere)
# numere.reverse()
# print(numere)

# copy - creeaza o copie superficiala a listei
#
# a=[1,2,3]
# b=a.copy()
# b.append(4)
# print(a)
# print(b)

# count() - numara de cite ori apare o valoare
# numere=[1,2,2,2,3]
# nume=["Ana", "Ana", "Florin"]
# aparitii=numere.count(2)
# aparut=nume.count("Ana")
# print(aparitii)
# print(aparut)

# min sau max- returneaza cea mai mica sau cea mai mare valoare
#
# numere=[1,2,3,4,5]
# print(min(numere))
# print(max(numere))

# sum () - aduna toate elementele numerice dintr-o lista

# numere=[1,2,3,4,5]
# total=sum(numere)
# print(total)

# zip() - combina doua sau mai multe liste element cu element

# nume=["ana","florin", "mihai"]
# note=[7,8,9]
# for nume, note in zip(nume,note):
#     print(nume,note)

# iterare prin lista
# for simplu
# nume=["ana", "florin", "mihai"]
# for persoana in nume:
#     print(persoana)


# iterare cu index

# nume=["ana","florin", "mihai"]
# for index in range(len(nume)):
#     print(index,nume[index])


# cu enumerate- parcurgi o lista si ai nevoie de doua lucruri in acelasi timp: indexul si valoarea

# fructe=["mere", "pere", "banane"]
#
# for index, valoare in enumerate(fructe):
#     print(index,valoare)

# exercitiu - gestionare comenzi magazin
# avem o lista pentru comenzile dintr-un magazin
# [nume_produs,pret,status]
# 1.sa afisam toate comenzile
# 2.afiseaza doar comenzile neprocesate
# 3. calculeaza valoarea totala a comenzilor
# 4. pune comenzile neprocesate ca procesate
# 5, afiseaza lista dupa modificari

comenzi=[
    ["telefon", 1000, "neprocesata"],
    ["laptop", 5000, "procesata"],
    ["aspirator", 2000, "neprocesata"]
]
# 1. Afiseaza toate comenzile

#
# lista_cumparaturi=["lapte", "carne","oua", "piine"]
# # 1. Afiseaza toate produsele
#
# for produse in lista_cumparaturi:
#     print(produse)
#
# # 2. Adauga produsul "iaurt"
# lista_cumparaturi.append("iaurt")
# print("ultimul element adaugat", lista_cumparaturi[-1])
# print(lista_cumparaturi)
#
# # 3. daca "piine" exista in lista, sterge produsul
# if "piine" in lista_cumparaturi:
#     lista_cumparaturi.remove("piine")
# print(lista_cumparaturi)
# # 4. Sortam lista la final
# lista_cumparaturi.sort()
# print(lista_cumparaturi)

# Exercitiu - lista numere
numere=[10,-3,5,0,-11,12,7,-1]
# 1. Afisam toate numerele
for numar in numere:
    print(numar)

# 2. O lista doar cu numere pozitive
nr_pozitive=[]
for numar in numere:
    if numar>=0:
        nr_pozitive.append(numar)
print(nr_pozitive)

# 3. o lista doar cu numere negative
nr_negative=[]
for numar in numere:
    if numar<0:
        nr_negative.append(numar)
print(nr_negative)

# 4. suma numerelor pozitive
suma_nr_pozitive=sum(nr_pozitive)
print(suma_nr_pozitive)

# 5. Sorteaza descrescator lista cu numere pozitive

print(suma_nr_pozitive)
# 1 var 1
nr_pozitive.sort()
# 2 var 2
nr_pozitive.sort(reverse=True)

print(nr_pozitive)

