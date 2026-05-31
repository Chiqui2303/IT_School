# dictionar=dict()

# d.keys[]- toate cheile
# d.values() - toate valorile
# d.items() - perechi cheie-valoare
# d.update(d2) - imbina cu alt dictionar
# d.copy() - copie superficiala
# d.clear() - sterge tot dictionarul
# "nume_cheie" in d - verifica existenta cheii

# d1={"a":1,"b":2}
# d2={"b":3,"c":4}
# d3=d1|d2 # reuniune dictionare - ia toate perechile cheie-valoare din d1 si d2 si creaz un dictionar nou
# print(d3)

# simbolul & -> intersectie

# a={1,2,3,4}
# b={2,3,4,5}
#
# print(a&b)
#
# d1={"a":1,"b":2}
# d2={"b":2,"c":4}
# print(d1.keys()&d2.keys())



# exercitii.

# creeaza un dictionar numit user cu informatiile:

# username
# e-mail
# varsta
# oras
# afisati informatiile pe rind
#
# user={
#     "username": "sorin",
#     "e-mail" : "niros2303@gmail.com",
#     "varsta":25,
#     "oras": "Buzau"
# }
#
# print("user", user["username"])
# print("e-mail", user["e-mail"])
# print("varsta", user["varsta"])
# print("oras", user["oras"])


# Exerctiul 2

# produs={
#     "nume": "Tastatura",
#     "pret": 250,
#     "stoc":10
# }

# modifica pretul la 220
# produs["pret"]=220
# print(produs)

# adauga "categorie" cu valoarea "periferice"
# produs["categorie"]="periferice"
# print(produs)

# scade stocul cu 1
# produs["stoc"]-=1
# print(produs)

# afiseaza dupa modificari
# print(produs)



# exercitiul 3 - folosind dictionarul de la ex 2
# citeste de la tastatura o cheie: daca cheia exista, afiseaza valoarea;
# daca nu exista, afiseaza "informatia nu exista"

# Var 1
# cheie=input("introduceti o cheie")
# valoare=produs.get(cheie,"informatia nu exista")
# print(valoare)

# var 2
# cheie=input("introduceti o cheie")
# if cheie in produs:
#     print(produs[cheie])
# else:
#     print("informatia nu exista")

# produs={
#     "nume": "Tastatura",
#     "pret": 250,
#     "stoc":10
# }

# daca pretul este mai mare de 100 se aplica reducerea 15% dupa care afisam pretul final
# print(f"Pret initial {produs["pret"]}")
# if produs["pret"]>100:
#     produs["pret"]=produs["pret"]*0.85
# print(f"Pretul dupa reducere {produs["pret"]}")

# exercitiul 5:
# produse={
#     "mouse":80,
#     "tastatura": 150,
#     "monitor" : 223,
#     "cablu" :110,
#     "casti":250
# }

# numara cite produse au pretul sub 200 si cite au pretul peste 200
#
# prod_ieftine=0
# prod_scumpe=0
# for pret in produse.values():
#     if pret<200:
#         prod_ieftine+=1
#     elif pret>=200:
#         prod_scumpe+=1
# print(f"Sint {prod_ieftine} produse ieftine.")
# print(f"Sint {prod_scumpe} produse scumpe.")



# exercitiul 6: vreau sa creez un dictionar folosind functia input,
# atit pentru chei cit si pentru valori astfel incit
# 1. Dictionarul sa aiba numar variabil de perechi
# 2. La final se printeaza dictionarul
#
dictionar={}
numar_perechi=int(input("Cite perechi adaugati"))

for chei in range(numar_perechi):
    cheie=input(f"Care este cheia nr. {chei} ?")
    valoare=input(f"Care este valoarea pentru cheia {cheie} ?")
    dictionar[cheie]=valoare
print("Dictionarul este", dictionar)




