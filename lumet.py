#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

#license GPLv3 copyleft

from math import *

class Application(object):
	def __init__(self):
		"""Constructeur de la fenêtre principale."""
		self.root=Tk()
		self.root.title('Lumet en python orienté objet')
		#self.calculeTempPot()
		Label(self.root, text="Température potentielle et vent géostrophique").grid(row=2,column=1,columnspan=3)
		
		#Un bouton pour lancer le calcul de la température potenielle et deux champs pour réccupérer les valeurs saisies par l'utilisateur
		Button(self.root, text="Théta", command=self.calculeTempPot).grid(row=3,column=1)
		Label(self.root, text="Température?").grid(row=3,column=3,columnspan=1)
		self.entreeT=Entry(self.root,width=14)
		self.entreeT.grid(row=3,column=2)
		Label(self.root, text="Pression?").grid(row=4,column=3,columnspan=1)
		self.entreeP=Entry(self.root,width=14)
		self.entreeP.grid(row=4,column=2)
		
		#Idem pour le calcul du vent géostrophique à partir des gradients de pression zonaux et méridiens
		Button(self.root, text="Géostrophie", command=self.calculeVentGeost).grid(row=7,column=1)
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
		
#Ce constructeur me fait me demander s'il faut que je code aussi des destructeurs???
		
	#Température potenielle, méthode de calcul	
	def calculeTempPot(self):
		"""Calcul de la température potentielle à partir de la température et de la pression atmosphérique"""
		self.v1ch=self.entreeT.get()
		self.v2ch=self.entreeP.get()
		try:
			T=float(self.v1ch)
			P=float(self.v2ch)
		except:
			err=1
		else:
			err=0
		if err==1:
			self.signaleErreur()
		#si la température rentrée est <100 alors on considère que l'on est en °C
		elif T<100: 
			self.turePot=(T+273.15)*(1000/P)**(287/1004.5)
		else:
			self.turePot=(T)*(1000/P)**(287/1004.5)
					
		self.afficheTempPot()	
		
	#Température potentielle: méthode d'affichage
	def afficheTempPot(self):
		"Affichage de la valeur de la température potentielle"
		Label(self.root, text="Theta = " + str(int(self.turePot)) + "K soit "+ str(int(self.turePot-273.15)) + "°C").grid(row=5,column=1,columnspan=3)
		
	#température potentielle: méthodes en cas d'erreur de saisie (l'utilisateur rentre qqchos d'autre qu'un nombre
	def signaleErreur(self):
		self.entreeT.configure(bg='red')
		self.root.after(1000,self.videEntree)
		
	def videEntree(self):
		self.entreeT.configure(bg='white')
		self.entreeT.delete(0,len(self.v1ch))
	
	#Vent géostrophique: méthode de calcul à partir des gradients de pressions rentrés par l'utilisateur
	def calculeVentGeost(self):
		"Calcul du vent géostrophique à partir des gradients de pression meridiens et zonaux"
		self.v1ch=self.entreePx.get()
		self.v2ch=self.entreePy.get()
		try:
			Px=float(self.v1ch)
			Py=float(self.v2ch)
		except:
			err=1
		else:
			err=0
		if err==1:
			self.signaleErreur()
		else:
			self.uGeo=(-1/(1.225*0.0001))*Px/1000
			self.vGeo=(1/(1.225*0.0001))*Py/1000
		
		self.roseDesVents()			
		self.afficheVentGeost()
	
	#Vent géostrophique: méthode de détermination du secteur dans lequel le vent souffle, bourrin, certes mais efficace :)
	def roseDesVents(self):
		"Rose des vents en fonction de la direction du vent géostrophique"
		self.angleDirection= atan2(self.uGeo,self.uGeo)*180/3.14159
		#Donne la direction en degré à partir de tan(self.angleDirection)=Ug/Vg que l'on passe en ArcTan et que l'on convertit en degré. Détermination de la direction du vent en utilisant le tri des secteurs. Les angles appartiennent à l'intervalle [0,180]U[-180,-0] 0 degré est un vent de Sud, + 90 est un vent d'Ouest, 180/-180 degré est un vent de Nord, -90 un vent d'Est.

		if ((self.angleDirection>=-11.25) and (self.angleDirection<=11.25)): #Secteur Sud si self.angleDirection compris entre -11.25 degré et +11.25 degré.
			self.secteurVent="Sud"
		elif ((self.angleDirection>11.25) and (self.angleDirection<33.75)):
			self.secteurVent="Sud/Sud-Ouest"
		elif ((self.angleDirection>=33.75) and (self.angleDirection<=56.25)):
			self.secteurVent="Sud-Ouest"
		elif ((self.angleDirection>56.25) and (self.angleDirection<78.75)):
			self.secteurVent="Ouest/Sud-Ouest"
		elif ((self.angleDirection>=78.75) and (self.angleDirection<=101.25)):
			self.secteurVent="Ouest"
		elif ((self.angleDirection>101.25) and (self.angleDirection<123.75)):
			self.secteurVent="Ouest/Nord-Ouest"
		elif ((self.angleDirection>=123.75) and (self.angleDirection<146.25)):
			self.secteurVent="Nord-Ouest"
		elif ((self.angleDirection>146.25) and (self.angleDirection<168.75)):
			self.secteurVent="Nord/Nord-Ouest"
		elif ((self.angleDirection>=168.75) and (self.angleDirection<=180)):
			self.secteurVent="Nord"
		elif ((self.angleDirection>=-180) and (self.angleDirection<=-168.75)):
			self.secteurVent="Nord"
		elif ((self.angleDirection>-168.75) and (self.angleDirection<-146.25)):
        		self.secteurVent="Nord/Nord-Est"
		elif ((self.angleDirection>=-146.25) and (self.angleDirection<=-123.75)):
			self.secteurVent="Nord-Est"
		elif ((self.angleDirection>-123.75) and (self.angleDirection<-101.25)):
			self.secteurVent="Est/Nord-Est"
		elif ((self.angleDirection>=-101.25) and (self.angleDirection<=-78.75)):
			self.secteurVent="Est"
		elif ((self.angleDirection>-78.75) and (self.angleDirection<-56.25)):
			self.secteurVent="Est/Sud-Est"
		elif ((self.angleDirection>=-56.25) and (self.angleDirection<=-33.75)):
			self.secteurVent="Sud-Est"
		elif ((self.angleDirection>-33.75) and (self.angleDirection<-11.25)):
			self.secteurVent="Sud/Sud-Est"
	
	#Vent géostrophique: méthode d'affichage des valeurs calculées.
	def afficheVentGeost(self):
		"Affichage de la valeur de la température potentielle"
		Label(self.root, text="Vent de module = " + str(int(sqrt(self.uGeo**2+self.vGeo**2))) + "m/s et de secteur "+ str(self.secteurVent)).grid(row=8,column=1,columnspan=3)


#programme principal
if __name__== '__main__':
	from tkinter import *
	from matplotlib import pyplot
	%matplotlib inline
	x=[1,2,3,4,5,6,7]
	pyplot.plot(x)
	#f=Application()
			
