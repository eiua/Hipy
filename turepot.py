#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

#license GPLv3 copyleft

from math import *

	#Température potenielle, méthode de calcul	
class TempPot():
	def __init__(self,x,y):
		self.T=x
		self.P=y
		self.turePot=0
        
	def calculeTempPot(self):
		"""Calcul de la température potentielle à partir de la température et de la pression atmosphérique"""
		#si la température rentrée est <100 alors on considère que l'on est en °C
		if self.T<100: 
			self.turePot=(self.T+273.15)*(1000/self.P)**(287/1004.5)
		else:
			self.turePot=(self.T)*(1000/self.P)**(287/1004.5)
            
	#Température potentielle: méthode d'affichage
	def afficheTempPot(self):
		"Affichage de la valeur de la température potentielle"
		print("Theta = " + str(int(self.turePot)) + "K soit "+ str(int(self.turePot-273.15)) + "°C")
#		print(self.turePot)

#programme principal
if __name__== '__main__':
    
    #Température potentielle pour -10°C à une altitude de 850hPa
    g=TempPot(-10,850)
    g.calculeTempPot()
    g.afficheTempPot()

