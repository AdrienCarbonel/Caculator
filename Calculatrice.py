import tkinter as tk
import math


fenetre_racine = tk.Tk()
# Fonctions

# Boutons pour les chiffres de 0 à 9
bouton0 = tk.Button(fenetre_racine,text="0",font=("helvetica","20"))
bouton1 = tk.Button(fenetre_racine,text="1",font=("helvetica","20"))
bouton2 = tk.Button(fenetre_racine,text="2",font=("helvetica","20"))
bouton3 = tk.Button(fenetre_racine,text="3",font=("helvetica","20"))
bouton4 = tk.Button(fenetre_racine,text="4",font=("helvetica","20"))
bouton5 = tk.Button(fenetre_racine,text="5",font=("helvetica","20"))
bouton6 = tk.Button(fenetre_racine,text="6",font=("helvetica","20"))
bouton7 = tk.Button(fenetre_racine,text="7",font=("helvetica","20"))
bouton8 = tk.Button(fenetre_racine,text="8",font=("helvetica","20"))
bouton9 = tk.Button(fenetre_racine,text="9",font=("helvetica","20"))

# Boutons pour les opérations
signe_plus = tk.Button(fenetre_racine,text="+")
signe_moins = tk.Button(fenetre_racine,text="-")
multiplication = tk.Button(fenetre_racine,text="x")
division = tk.Button(fenetre_racine,text="/")
racine_carre = tk.Button(fenetre_racine,text="sqrt(x)",command= math.sqrt)
egal = tk.Button(fenetre_racine,text= "=")

# Affichage des Boutons

# Ecran de Calculatrice