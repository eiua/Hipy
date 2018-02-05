class Personnage():
    def __init__(self,pos,v):
        self.position=pos
        self.vie=v
        
    def soigner(self,unPerso):
        unPerso.vie += 10