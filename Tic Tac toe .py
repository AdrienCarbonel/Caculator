from turtle import*


def carre():
    for i in range(1,5):
        forward(100)
        left(90)
        

# Grille du Morpion
for i in range(3):
    for j in range(3):
        carre()
        forward(100)

