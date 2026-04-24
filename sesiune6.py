# instructiunea for
for i in range(6):
    print("Salut")

# sintaxa generala
# for variabila in colectie
#       ins

for i in range(5):
    print(i)

# range(5) -> nu inseamna de la 1 pina la 5
# porneste de la 0
# se opreste inainte de 5


for i in range(1,10,2):
    print(i)

# range are 3 variante
# range(stop) -> range(5)
# range(start, stop) -> range (0,5)
# range (start, stop, pas) -> range (0,5,2)


for i in range(2, 6):
    print(i)

for i in range(0, 10, 2):
    print(i)

#  pas negativ

for i in range(10, 0, -1):
    print(i)

#  variabila din for
# i este o variabila care primeste pe rind valorile

# exemplu
for i in range(5):
    print(i+10)

for i in range(3):
    x=i+2
    print(x)
print("sfirsit")

for i in range(3):
    print(i)
    print("salut")

#
a=10

for i in range(3):
    print(a+i)

for i in range(6):
    if i%2==0:
        print(i)

for i in range(5):
    if i<3:
        print(f"{i} - valoare mica")
    else:
        print(f"{i} - valoare mare")


for i in range(5):
    if i ==3:
        print("am gasit 3")
    print(i)

for i in range (10):
    if i>2 and i<6:
        print(i)

#  break /Continue in For

for numar in range(1,6):
    if numar ==3:
        break
    print(numar)

for numar in range(1,6):
    if numar == 3:
        continue
    print(numar)

for litera in"python":
    if litera =="h":
        break
    print(litera)

for litera in"python":
    if litera =="h":
        continue
    print(litera)

# sa se calculezwe suma tuturor numerelor pare de la 1 la 20 (inclusiv)
suma=0
for i in range(1,21):
    if i%2 ==0:
        suma = suma+i
print(suma)

# 2. sa se parcurga nr de la 1 la 30 inclusiv si sa se afiseze cite numere sint pare si >10

counter=0
for i in range(1,31):
    if i>10 and i%2==0:
        counter= counter+1
    print(counter)
print("total",counter)

# 3 sa se calculeze suma numerelor de la 1 la 100 care sint divizibile si cu 3 si cu 5

suma =0
for i in range(1,101):
    if i%3==0 and i%5==0:
        suma =suma +i
#       suma+=i
print("suma este ", suma)

# 4 sa se parcurga numerele de la 1 la 10. pt fiecare numar se calculeaza rezultat=i*3-2. sa se afle cea mai mare valoare obtinuta.
maxim =0
for i in range(1,11):
    rezultat =i*3-2
    if rezultat> maxim:
        maxim =rezultat
        print(maxim)
print("cea mai mare valoare e",maxim)

# 5 se da un text. pentru fiecare vocala incrementam cu 2 pct, iar pentru fiecare consoana cu 1 pct. la final afiseaza total pct
text="python"
puncte=0
for litera in text:
    if litera =="a" or litera =="e" or litera =="i" or litera =="o" or litera =="u":
        puncte=puncte+2
    else:
        puncte=puncte+1
    print(puncte)
print("total", puncte)




