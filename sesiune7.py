import random

# while conditie:
    # bloc de cod

# x=0
# while x<5:
#     print(x)
#     x+=1
#
# while true:
#     print("ruleaza la infinit!")
#

# else in while
# x=0
# while x<3:
#     print(x)
#     x+=1
# else:
#     print("while s-a terminat natural")
#
# conditie=""
# while conditie!="exit":
#     conditie=input("scrie 'exit' pt iesire")

# while True:
#     comanda=input("comanda:")
#     if comanda =="stop":
#         break
#     print("Ai testat:", comanda)

    # Blocul try/except
# try:
#     x=10/0
# except ZeroDivisionError:
#     print("nu poti imparti la zero")

# exemplu
# try:
#     numar=(int("introdu un nr"))
#     print("numarul")
# except ValueError:
#     print("  ")

# numar=2
# while numar<=20:
#     divizor=2
#     prim =True
#     while divizor <numar:
#         if numar%divizor==0:
#             prim=False
#             break
#         divizor+=1
#     if prim:
#         print(numar)
#     numar+=1

# ghiceste numarul

# numar_secret=7
# ghicire=None
# while ghicire != numar_secret:
#     ghicire=int(input("ghiceste numarul"))
#     print("Ai ghicit!")

# numar_secret = random.randint(1,100)
# ghicire = None
# incercari=0
# incercari_maxime=5
# while ghicire!= numar_secret and incercari<=incercari_maxime:
#     try:
#         ghicire = int(input(f"ghiceste numarul(1-10). Ai {incercari_maxime} incercari "))
#         incercari+=1
#         if ghicire<numar_secret:
#             print("numarul este mai mare")
#         elif ghicire>numar_secret:
#             print("numarul este mai mic")
#     except ValueError:
#         print("Introdu un numar valid")
#         continue
# if ghicire==numar_secret:
#     print(f"Ai ghicit din {incercari} incercari!")
# else:
#     print(f"Ai pierdut, numarul era: {numar_secret}")


# exercitiu:
# Simulator bancomat
# Avem un sold initial de 1000 lei. vrem sa afisam un meniu:
# 1. vezi sold
# 2 . depune bani
# 3. retrage bani
# 4. iesire
# reguli
# 1. meniul trebuie repetat pina cind userul alege iesirea
# 2 la retragere, nu ai voie sume mai mari decit soldul
# 3.fara sume negative sau zero
# 4. dupa fiecare operatie afisezi soldul nou

sold=1000.0
aplicatia_ruleaza=False
pin_corect="1234"
incercari_maxime=3
autentificat=False
incercari=0
while incercari<incercari_maxime:
    pin_introdus=input("Introduceti PIN: ")
    if len(pin_introdus)!=4:
        print("PIN trebuie sa contina 4 cifre!")
        incercari+=1
        incercari_ramase=incercari_maxime-incercari
        print(f"Incercari ramase: {incercari_ramase}")
        continue

    if pin_introdus==pin_corect:
        print("Autentificat")
        autentificat=True
        break
    else:
        incercari+=1
        incercari_ramase = incercari_maxime - incercari
        print("PIN incorect")
        print(f"Incercari ramase: {incercari_ramase}")

if autentificat==False:
    print("Card blocat. Prea multe incercari!")
if autentificat==True:
    aplicatia_ruleaza =True

    while aplicatia_ruleaza:
        print("\n****MENIU****")
        print("1. Vezi Sold")
        print("2. Depune bani")
        print("3.Retrage bani")
        print("4. Iesire")
        print("*************\n")

        optiune=input("Alege o optiune (1-4)")
        if optiune=="1":
            print(f"Soldul curent este {sold:.2f} LEI")
        elif optiune=="2":
            suma_text=input("Introduceti suma pe care vreti sa o depuneti:")
            try:
                suma=float(suma_text)
                if suma<=0:
                    print("Suma trebuie sa fie mai mare decit 0")
                else:
                    sold=sold+suma
                    print(f"Ati depus suma de {sold:.2f} lei.")
                    print(f"Noul sold este: {sold:.2f} lei.")
            except ValueError:
                print("Valoare invalida. Introduceti un numar valid.")
        elif optiune=="3":
            suma_text = input("Introduceti suma pe care vreti sa o retrageti:")
            try:
                suma = float(suma_text)
                if suma <= 0:
                    print("Suma trebuie sa fie mai mare decit 0")
                elif suma>sold:
                    print("Fonduri insuficiente")
                    print(f"Soldul dumneavoastra este {sold:.2f} Lei.")
                else:
                    sold = sold - suma
                    print(f"Ati retras suma de {sold:.2f} lei.")
                    print(f"Noul sold este: {sold:.2f} lei.")
            except ValueError:
                print("Valoare invalida. Introduceti un numar valid.")
        elif optiune=="4":
            print("Iesire din meniu")
            aplicatia_ruleaza = False
        else:
            print("Optiune invalida")





