################################
#Information sur le froupe
#MIASHS L1S2 TD1
#Groupe 2
#Yannis KYRIASIS
#Nadir HADEOUI
#Ismael AYAD
#Oumou ATJI
#https://github.com/uvsq22004651/projet_incendie
################################

################################
# Importations de librairies

import tkinter as tk 


################################
# Constantes


################################
# Fonctions

def quadrillage():
    """Création du quadrillage"""
    for l in range(0, 601, 10):
        for h in range(0, 401, 10):
            canvas.create_line((0, h), (600, h), fill='black')
            canvas.create_line((l, 0), (l, 400), fill='black')

################################
# Programme principale
racine = tk.Tk()
racine.title("Incendie")


################################
# Création des widgets

canvas = tk.Canvas(racine, width=600, height=400, bg="white")




################################
# Placement des widegts

canvas.grid(column=0, row=0)

bouton_commencer = tk.Button(racine, text="Commencer", command=quadrillage)
bouton_commencer.grid()


racine.mainloop()
