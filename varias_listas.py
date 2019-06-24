
nummero_introducido = input("Tell me a number: (Write pi to finish): ")
lista_uno = []
multiplos_dos = []
multiplos_tres = []
multiplos_cinco = []
multiplos_siete = []

while nummero_introducido != "3.1416" :
    lista_uno.append(int (nummero_introducido))
    nummero_introducido = input("Tell me a number: (write pi to finish): ")

for indice in range(len(lista_uno)):

    if lista_uno[indice] % 2 == 0:
        multiplos_dos.append(lista_uno[indice])
    if lista_uno[indice] % 3 == 0:
        multiplos_tres.append(lista_uno[indice])
    if lista_uno[indice] % 5 == 0:
        multiplos_cinco.append(lista_uno[indice])
    if lista_uno[indice] % 7 == 0:
        multiplos_siete.append(lista_uno[indice])
print("Your list is {}".format(lista_uno))
print("Multiplos 2 {}".format(multiplos_dos))
print("Multiplos 3 {}".format(multiplos_tres))
print("Multiplos 5 {}".format(multiplos_cinco))
print("Multiplos 7 {}".format(multiplos_siete))

