class vehicule:
    def __init__(self,marque,qEssance):
        self.marque=marque
        self.qEssance=qEssance

    def affiche_marque(self):
        print(self.marque)

    def deplacer(self):
        print(' la voiture',self.marque,'a fait un pa en avant')


class voiture(vehicule):

    def __init__(self,marque,vqEssance,model,rapport):
        vehicule.__init__(self,marque,vqEssance)
        self.model=model
        self.rapport=rapport

    def deplacer(self):
        print( ' la voiture',self.model,'a fait un pa en avant ')
#program

v=voiture('benz',50,'serie une',6)
v.affiche_marque()
v.deplacer()
