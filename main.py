"""""
Liam Rodriguez
2024-03-13
Jeu de devinette
"""""

import random

nombre_perso = 0
end = True
print("Votre but est de devinner le nombre que j'ai choisi.")
#Choisir un chifre

while end:
    nombre_ordi = random.randint(1, 10)

    while nombre_ordi != nombre_perso:
        nombre_perso = int(input("Essayer de devinner le nombre:"))

        if nombre_ordi > nombre_perso:
            print("votre chiffre est plus petit que le mien")

        elif nombre_ordi < nombre_perso:
            print("Votre nombre est plus grand que le mien")

        elif nombre_ordi == nombre_perso:

            print("Vous avez deviner!")
            ask = input("Veux tu recomencer? Y/N")
            if ask == "Y":
                print("ok :D")

            if ask =="n":
                exit()


