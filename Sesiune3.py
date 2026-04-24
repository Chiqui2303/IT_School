from enum import nonmember
from operator import truediv

nume="ana"
varsta=20
inaltime=1.60
print("salut")
print(nume)
print(nume,varsta)
#putem afisa si text si variabile
print("numele meu este:", nume)

#mai multe moduri de afisare cu print
#var 1 -
print(nume,varsta)
#var2 cu +
prenume="ion"
nume_familie="popescu"
print(prenume +" " + nume_familie)
# cu + ambele variabile trebuie sa fie stringuri

# ok
oras="buzau"
print("Locuiesc in "+ oras)

# NOK
varsta=25
# print("Am" + varsta + "ani")
# varaianta corectata
print("AM " + str(varsta) + " ani")

# var 3
nume="Sorin"
varsta=52
print(f"Numele meu este {nume} si am {varsta} ani")
# litera f

# var 4
nume ="Elena"
varsta=25
oras = "Buzau"
print("Ma numesc {} si am {} ani din {}".format (nume, varsta, oras))

# exercitiu 1
print()
# exercitiu 2 - creaza 2 variabile nume si oras , apoi afiseaza pe aceeasi linie
nume= "Sorin"
oras = "Buzau"
print(f"{nume} din {oras}")
print(nume + " din " + oras)
print(nume ,"din", oras)
text = "Sorin"
print(len(text))
# tipuri de date in Python
# un tip de date arata ce fel de valoare avem intr-o varaiabila
# un nume este text
# varsta este un numar intreg
# o inaltime este un numar zecimal/flotant
# o valoare de tip da/nu poate fi adevarata sau falsd
# python trebuie sa stie ce fel de informatie pastreaza pentru fiecare tip de date ,
nume ="ana"
oras ="cluj"
mesaj= "Salut"
a= "Python"
b='curs'
# obs chiar daca scriem cifre intre ghilimele, vor fi considerate tot text
# triple quotes - pentru stringuri care contin mai multe rinduri
text= """"Acesta este text 
care contine mai 
multe rinduri"""
print(text)
print(type(text))
nume = "Sorin"
text= f""""Acesta este text 
cu {nume}
multe rinduri"""
print(text)

# \n inseamna 'treci pe linia urmatoare'
print("Salutare\nBine ai venit\nLa curs")
print("\nSalutare\nBine ai venit\nLa curs")
print("Meniu\n1. Pizza\n2. Paste\n3. Sucuri")
Varsta=25
an =2026
numar_persoane=16
# float - numar zecimal
inaltime=1.75
pret=19.99
temperatura=15.5
print(15.5)
print(temperatura)
# bool- boolean - adevarat sau fals
invata_python = True
este_ziua_mea=False

variabila = None
