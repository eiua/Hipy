#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

#license GPLv3 copyleft

from tkinter import *

from turepot import *
from ventgeost import *

class Application():
	def __init__(self):
		"""Constructeur de la fenêtre principale."""
		self.root=Tk()
		self.root.title('Lumet en python POO')
	
		#Un bouton pour lancer le calcul de la température potenielle et deux champs pour réccupérer les valeurs saisies par l'utilisateur
		Button(self.root, text="Théta", command=self.declencherTempPot).grid(row=3,column=1)
		Label(self.root, text="Température?").grid(row=3,column=3,columnspan=1)
		self.entreeT=Entry(self.root,width=14)
		self.entreeT.grid(row=3,column=2)
		Label(self.root, text="Pression?").grid(row=4,column=3,columnspan=1)
		self.entreeP=Entry(self.root,width=14)
		self.entreeP.grid(row=4,column=2)
	
		#Idem pour le calcul du vent géostrophique à partir des gradients de pression zonaux et méridiens
		Button(self.root, text="Géostrophie", command=self.declencherVentGeost).grid(row=7,column=1)
		Label(self.root, text="GradPx?").grid(row=6,column=3,columnspan=1)
		self.entreePx=Entry(self.root,width=14)
		self.entreePx.grid(row=6,column=2)
		Label(self.root, text="GradPy?").grid(row=7,column=3,columnspan=1)
		self.entreePy=Entry(self.root,width=14)
		self.entreePy.grid(row=7,column=2)
	
		#Un boutton pour fermer le logiciel
		Button(self.root, text="Quitter", command=self.root.quit).grid(row=1,column=3)
		
		#lancer la boucle infinie de l'interface
		self.root.mainloop()
	
	def declencherTempPot(self):
		"déclencher le calcul de la température potentielle"
				
		t=TempPot(float(self.entreeT.get()),float(self.entreeP.get()))
		t.calculeTempPot()
		
		Label(self.root, text="Theta = " + str(int(t.turePot)) + "K soit "+ str(int(t.turePot-273.15)) + "°C").grid(row=5,column=1,columnspan=3)
		
	def declencherVentGeost(self):
		"déclencher le calcul du vent géostrophique"
		v=VentGeost(float(self.entreePx.get()),float(self.entreePy.get()))
		v.calculeVentGeost()
		v.roseDesVents()
		
		Label(self.root, text="Vent de module = " + str(int(sqrt(v.uGeo**2+v.vGeo**2))) + "m/s et de secteur "+ str(v.secteurVent)).grid(row=8,column=1,columnspan=3)

			
#programme principal
if __name__== '__main__':
	f=Application()
