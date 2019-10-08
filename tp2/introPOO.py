class humain:
    def __init__(self,nomm,agee):
        self.nom=nomm
        self.age=agee
        humain.nombreHumain+=1

    def direTruc(self,a): #method simple
        print(self.nom,'a dit',a)

    nombreHumain = 0 # attribut de class

    def doublerNombre(cls):
        humain.nombreHumain*=2

    doublerNombre = classmethod(doublerNombre) # methode de classe (tji b CLS apres ndiro attribut de class)

    def definition():
        print("L\'Humain est un etre 3aaaayaaaan x))))")

    definition = staticmethod(definition) #method statid .. public stativ void ..


#program

a=humain('mehdi',22)
a.direTruc("saha les hommes")
b=humain('sa3id',22)
b.direTruc('cava chwia labas bikhir')
print(humain.nombreHumain)
humain.doublerNombre()
print(humain.nombreHumain,k)
humain.definition()