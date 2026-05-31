# matrice / Liste imbricate / nested lists / lista in lista
# matrice=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# accesare elemente lista inlantuita
# Acesare prin lista interioara
# print("1. matrice[0] accesam prima lista interioara", matrice[0])

# Accesez un element din lista interioara
# print("2.matrice[0][1] accesam al doilea element din prima lista interioara", matrice[0][1])

# modificarea unui element
# matrice[1][1]=99
# print(matrice)

clase=[
    ["Ana","Mihai","Ioana"],
    ["George","Maria","Andrei"],
    ["Alex","Diana", "Paul"]
]

# parcurgerea listei inlantuite cu for

# for clasa in clase:
#     print(clasa)
#
# for clasa in clase:
#     for element in clasa:
#         print(element)

# Exemplu
# situatie_elevi=[
#     ["Ana",10,9,8],
#     ["Mihai",8,8,9],
#     ["Ioana",10,10,9]
# ]
# print(situatie_elevi)
# for elev in situatie_elevi:
#     nume=elev[0]
#     note_elev=elev[1:]
#     media=sum(note_elev)/len(note_elev)
#     print(f"{nume} are media {media:.2f}")

# adaugare intr-o lista nested

# clase=[
#     ["Ana","Mihai","Ioana"],
#     ["George","Maria","Andrei"],
#     ["Alex","Diana", "Paul"]
# ]
# print(clase)
# clase[0].append("Florin")
# print(clase)

# adaugare lista noua
# clase.append(["Marius", "Cosmin"])
# print(clase)

# afiseaza diagonala principala si secundara in matrice
# matrice=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# diagonala principala
#
# for index in range(len(matrice)):
#     print(matrice[index][index])

# diagonala secundara
#
# n=len(matrice)
#
# for index in range(len(matrice)):
#     print(matrice[index][n-1-index])

# creeaza o lista cu 10 numere si afiseaza doar elementele de pe pozitiile pare

# intro=input("introduceti 10 numere")
# lista=list(intro)
lista=[2,6,9,11,2,20,13,76,33,8]
for i in range(len(lista),2):
    print(lista[i])

print(f"Elementele de pe pozitii pare sint: {lista[::2]}")

# 2. adauga un element nou la sfirsitul listei
lista.append(85)
lista+=[43]
print(lista)

# 3. schimba al doilea element din lista cu 99
lista[1]=99
print(lista)

# 4. afiseaza lungimea listei
print(len(lista))

# 5. Sorteaza lista crescator si apoi descrescator
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

# 6. Inverseaza lista fara sa folosesti reverse()

print(lista[::-1])

# 2. Folosind lista de mai jos, afiseaza doar cuvintele mai lungi de 3 litere
# si adauga_le intr-o noua lista
lista_cuvinte=["studentii", "mei", "stiu", "Python", "foarte", "bine"]
lista_cuv=[]
for cuvint in lista_cuvinte:
    if len(cuvint)>3:
        lista_cuv.append(cuvint)
print(lista_cuv)
