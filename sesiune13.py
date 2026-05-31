# un dictionar este o structura de date care stocheaza informatii
# sub forma de perechi cheie valoare.
# fiecare informatie se identifica printr-o cheie
# persoana={
#     "nume":"Andrei",
#     "varsta":25,
#     "oras":"Cluj"
# }

# comparatie Lista - Dictionar
# persoana_lista=["Andrei", 25, "Cluj"]
#
# print(persoana_lista[0])
# print(persoana_lista[1])
# print(persoana_lista[2])


# Dictionar
# print(persoana["nume"])
# print(persoana["varsta"])
# print(persoana["oras"])

# Folosim dictionare atunci cind vrem sa reprezentam date care au o structura clara

# crearea unui dictionar
# student={}
# print(student)
# student["nume"]="Florin"
# print(student)
# student["varsta"]=26
# student["oras"]="Cluj"
# print(student)

# dictionar cu valori initiale
# persoana={
#     "nume":"Andrei",
#     "varsta":25,
#     "oras":"Cluj"
# }


# chei si valori - in dictionar exista 2 componente importante - cheie:valoare
# telefon={
#     "brand":"Samsung",
#     "model":"Note10",
#     "pret":4200
# }

# tipuri de date pentru chei
# cel mai des folosim chei de tip str

# calificative={
#     1:"insuficient",
#     2:"suficient",
#     3:"bine"
# }

# print(calificative[2])


# tipuri de date pentru valori-- string, float, boolean,lista,etc

# Accesare valori din dictionar- pentru a acesa o valoare folosim cheia
# persoana={
#     "nume":"Andrei",
#     "varsta":25,
#     "oras":"Cluj"
# }

# print(persoana["nume"])

# 1. Python cauta cheia "nume" in dictionar si returneaza valoarea asociata

# daca cheia nu exista
# print(persoana["experienta"]) #-KeyError - accesam o cheie care nu exista

# metoda get()- putem accesa o valoare fara sa primim o eroare - va returna None daca cheia nu exista
# print(persoana.get("experienta"))
# print(persoana.get("nume"))

# la metoda get(), adaugam valoare implicita
# print(persoana.get("experienta", "nu exista cheia experienta"))

# cum verificam o cheie - operatorul in
# if "nume" in persoana:
#     print(persoana.get("nume"))
# else:
#     print("numele lipseste")
#
# print("Andrei" in persoana) #- False pentru ca "Andrei" este valoare nu cheie
#
# print(persoana.values()) # returneaza valorile din dictionar
# print(persoana.keys()) # returneaza cheile din dictionar
# print(persoana.items()) # returneaza in perechi cheia cu valoarea asociata din dictionar

# comparatii

# print("nume" in persoana) # True - cauta cheia
# print("Andrei" in persoana) # False - cauta cheia "Andrei" nu valoarea
# print(persoana.values()) # True - cauta valoarea
# print(persoana.keys()) # True - cauta cheia

# Adaugare perechi noi in dictionar
# persoana["sector"]=1
# print(persoana)

# Modificare valoare existenta
# persoana["nume"]= "mihai"
# print(persoana)

# stergere elemente din dictionar
#  del
# del persoana["sector"]
# print(persoana)

# metoda pop() - sterge cheia si returneaza valoarea stearsa
# persoana["sector"]=1
# print(persoana)
# cheie_stearsa=persoana.pop("sector")
# print(cheie_stearsa)
# print(persoana)

# metoda clear - sterge toate elementele din dictionar
# persoana.clear()
# print(persoana)

# adaugare cu append - doar daca o cheie are valori tip lista
# persoana["varsta"].append(27)

# parcurgerea unui dictionar - 3 variante
# parcurgem cheile
# parcurgem valorile
# le parcurgem pe amindoua in acelasi timp

# parcurgerea cheilor
# persoana={
#     "nume":"Andrei",
#     "varsta":25,
#     "oras":"Cluj"
# }

# for cheie in persoana:  # cind parcurgem direct dictionarul, automat se parcurg cheile
#     print(cheie)

# parcurgerea valorilor
# for valoare in persoana.values(): # returneaza valorile din dictionar
#     print(valoare)

# parcurgerea cheilor si valorilor
# for cheie,valoare in persoana.items(): # in bucla python desparte fiecare pereche in doua variabile: cheie,valaoare
#     print(f"{cheie} -> {valoare}")

# metode importante pentru dictionare
# 1. keys() - returneaza cheile
# 2. values() - returneaza valorile
# 3. items() - returneaza perechile cheie valoare
# 4. update() - actualizeaza un dictionar cu date din alt dictionar

# date_noi={
#     "oras":"Timisoara",
#     "inaltime":1.92
# }
# persoana.update(date_noi)
# print(persoana)

#dictionare cu liste ca valori
elev={
    "nume":"Florin",
    "note":[8,9,10]
}

# putem accesa lista
# print(elev["note"])

# putem accesa si o nota individuala din lista
# print(elev["note"][0])

# adaugarea unei valori intr-o lista din dictionar
# elev["note"].append(7)
# print(elev)

# lista de dictionare
# fiecare element din lista este un dictionar
studenti=[
    {
        "nume":"Andrei",
        "nota":9
    },
    {
        "nume":"Florin",
        "nota":4
    },
    {
        "nume":"Denisa",
        "nota":10
    }
]

# parcurgere lista de dictionare
# for student in studenti:
#     print(student["nume"],student["nota"])

# dictionar de dictionare
# produse={
#     "produs1":{ # produs1 -> dictionar cu date despre PC
#         "nume":"PC",
#         "pret":10000
#     },
#     "produs2":{ # produs2 -> dictionar cu date despre TV
#         "nume":"TV",
#         "pret":4000
#     }
# }

# Accesam pretul PC
# print(produse["produs1"]["pret"])# ia valoarea de la cheia "pret" din dictionarul produsului

# exemplu baza de date simpla - dictionar de dictionare
# useri={
#     "admin": {
#         "parola": "admin",
#         "rol": "administrator"
#     },
#     "user":{
#         "parola":"user123",
#         "rol":"utilizator"
#     }
# }
#
# username=input("username: ")
# parola=input("parola: ")
#
# if username in useri:
#     user=useri[username]
#     if parola==user["parola"]:
#         print("Autentificare OK")
#         print(f"Rol: {user["rol"]}")
#     else:
#         print("Parola gresita")
# else:
#     print("Userul nu exista")

# copierea dictionarelor varianta NOK

# student1={
#     "nume":"Andrei",
#     "nota":9
# }
#
# student2=student1
# student2["nota"]=10
#
# print(student1)
# print(student2)
#
# print(id(student1))
# print(id(student2))

# copierea dictionarelor varianta OK

# student1={
#     "nume":"Andrei",
#     "nota":9
# }
#
# student2=student1.copy()
# student2["nota"]=10
#
# print(student1)
# print(student2)
#
# print(id(student1))
# print(id(student2))



