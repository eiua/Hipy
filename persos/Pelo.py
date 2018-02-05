from Personnage import Personnage

class Pelo(Personnage):
    def __init__(self,n,f,pos,v):
        self.nom=n
        self.pognon=f
        #Attention, le super qui renvoie l'init de la superclasse parente doit être dans l'init de la classe fille!!
        super(Pelo,self).__init__(pos,v)
        
    def rentreePognon(self,ahh):
        self.pognon += ahh
    
    def sortiePognon(self,ohh):
        self.pognon -= ohh
    
    def faireLesComptes(self):
        print (self.pognon)
    
    def direNom(self):
        print(self.nom)