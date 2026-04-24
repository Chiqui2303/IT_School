# import sys
# print(sys.version)

x=25
y=int(x)
print(x+5)

x = "19.99"
print(type(x))
decimal = float(x)
print(type(decimal))

a=10
b=5

# Adunare
suma=a+b
print(suma)

# scadere
diferenta = a-b
print(diferenta)

# inmultire
produs=a*b
print(produs)

# impartire

cat=a/b
print(cat)
print(int(cat))

rezultat=10/3
print (rezultat)
print(f'{rezultat:.4f}')

# impartirea intreaga

print(10//3)

# restul impartirii

print(10%3)
#daca numarul rezultat este impar se afiseaza 1
print(8%2)
# daca numaul rezultat este par se afiseaza 0

# ridicarea la putere

print(2**3)
print(5**2)

# ordinea operatiilor
print(2+3*4)
print((2+3)*4)

# input() - cum citim date de la utilizator
# nume=input("Cum te numesti ? ")
# print(nume)
# virsta=input("Citi ani ai? \n")
# print(virsta)
# print(type(virsta))

# varsta=int(input("Citi ani ai?"))
# print(varsta)
# print(type(varsta))

# inaltime=float(input("Ce inaltime ai?"))
# print(inaltime)
# print(type(inaltime))

# numar1=input("Primul numar: ")
# numar2=input("Al doilea numar: ")

# print(numar1+numar2)

# numar1=int(input("Primul numar: "))
# numar2=int(input("Al doilea numar: "))

# print(numar1+numar2)

a = 10
b = 3
print("Adunare:", a + b)
print("Scadere:", a - b)
print("Inmultire:", a * b)
print("Impartire:", a / b)
print("Impartire intreaga:", a // b)
print("Restul impartirii:", a % b)
print("Puterea:", a ** b)

#1. Citeste de la tastatura numele utilizatorului si afiseaza un mesaj: Bun venit la curs, X

# nume=input("Numele tau este: ")
# print(f"Bine ai venit la curs {nume}.")

#2. Citeste de la tastatura 2 numere intregi si afiseaza suma lor

numar1=int(input("Primul numar este: "))
numar2=int(input("Al doilea numar este: "))
suma=numar1+numar2
print(f'Suma numerelor este {suma}.')
diferenta=numar1-numar2
print(f"Diferenta este {diferenta}.")
produs=numar1*numar2
print(f"Produsul este {produs}.")
cat=numar1/numar2
print(f"Rezultatul impartirii este {cat}.")

#4. Citeste varsta si afiseaza peste 5 ani vei avea X ani
varsta=int(input("Citi ani ai?"))
Varsta = varsta+5
print(f"Peste cinci ani vei avea {Varsta} ani.")

#5. Citeste un pret si o cantitate si calculeaza costul final

pret=float(input("pretul este: "))
cantitate=int(input("Cantitatea este de: "))
cost=pret*cantitate
print(f"Costul final este de {cost} lei.")
print(f"Costul produselor este de {cost:.2f} lei.")

