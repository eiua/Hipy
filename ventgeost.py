#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

#license GPLv3 copyleft

from math import *

class VentGeost():
	"""Vent géostrophique: méthode de calcul à partir des gradients de pressions rentrés par l'utilisateur"""
	def __init__(self,x=0,y=0):
		self.gradPx=x
		self.gradPy=y
		self.uGeo,self.vGeo,self.angleDirection=0,0,0
		self.secteurVent="coucou"
        
	def calculeVentGeost(self):
		"Calcul du vent géostrophique à partir des gradients de pression meridiens et zonaux"
		self.uGeo=(-1/(1.225*0.0001))*self.gradPx/1000
		self.vGeo=(1/(1.225*0.0001))*self.gradPy/1000

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
		print("Vent de module = " + str(int(sqrt(self.uGeo**2+self.vGeo**2))) + "m/s et de secteur "+ str(self.secteurVent))
		
#programme principal
if __name__== '__main__':
    
    #Vent géostrophique pour des gradients zonaux et méridiens de respectivement 2 et 3 hPa sur 100km
    f=VentGeost(2,3)
    f.calculeVentGeost()
    f.roseDesVents()
    f.afficheVentGeost()
