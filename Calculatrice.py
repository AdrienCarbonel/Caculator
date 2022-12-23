import tkinter as tk
import math


fenetre_racine = tk.Tk()
fenetre_racine.geometry("1920x1080")
calcul = ""
# Fonctions
def ajout_calcul(symbol):
    global calcul
    calcul += str(symbol)
    ecran.delete(1.0,"end")
    ecran.insert(1.0,calcul)

def eval_calcul():
    global calcul
    try:
        calcul = str(eval(calcul))
        ecran.delete(1.0,"end")
        ecran.insert(1.0,calcul)
    except:
        effacer_calcul()
        ecran.insert(1.0,"Erreur!")

def effacer_calcul():
    global calcul
    calcul = ""
    ecran.delete(1.0,"end")

# Ecran de Calculatrice

ecran = tk.Text(fenetre_racine,height=2,font=("helvetica",20))
    
# Boutons pour les chiffres de 0 à 9
bouton0 = tk.Button(fenetre_racine,text="0",font=("helvetica","20"),command= lambda: ajout_calcul(0))
bouton1 = tk.Button(fenetre_racine,text="1",font=("helvetica","20"),command=lambda: ajout_calcul(1))
bouton2 = tk.Button(fenetre_racine,text="2",font=("helvetica","20"),command=lambda: ajout_calcul(2))
bouton3 = tk.Button(fenetre_racine,text="3",font=("helvetica","20"),command=lambda: ajout_calcul(3))
bouton4 = tk.Button(fenetre_racine,text="4",font=("helvetica","20"),command=lambda: ajout_calcul(4))
bouton5 = tk.Button(fenetre_racine,text="5",font=("helvetica","20"),command=lambda: ajout_calcul(5))
bouton6 = tk.Button(fenetre_racine,text="6",font=("helvetica","20"),command=lambda: ajout_calcul(6))
bouton7 = tk.Button(fenetre_racine,text="7",font=("helvetica","20"),command=lambda: ajout_calcul(7))
bouton8 = tk.Button(fenetre_racine,text="8",font=("helvetica","20"),command=lambda: ajout_calcul(8))
bouton9 = tk.Button(fenetre_racine,text="9",font=("helvetica","20"),command=lambda: ajout_calcul(9))

# Boutons pour les opérations
signe_plus = tk.Button(fenetre_racine,text="+",command= ajout_calcul)
signe_moins = tk.Button(fenetre_racine,text="-",command= ajout_calcul)
multiplication = tk.Button(fenetre_racine,text="x",command= ajout_calcul)
division = tk.Button(fenetre_racine,text="/",command= ajout_calcul)
racine_carre = tk.Button(fenetre_racine,text="sqrt(x)",command= math.sqrt)
egal = tk.Button(fenetre_racine,text= "=",command= eval_calcul)

# Affichage des Boutons
ecran.grid()
bouton1.grid(row = 1,column = 0,columnspan=1,pady=10)
bouton2.grid(rowspan = 1,pady= 10)
bouton3.grid(rowspan=2,pady=10)
bouton4.grid(row=1,column=1)
bouton5.grid(rowspan=1,column=0)


fenetre_racine.mainloop()