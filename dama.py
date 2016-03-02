###### Razred GUI: <h4>
##Vmesnik bo vseboval metode, s katerimi bo risal poteze na platno. Celotni razred skupaj z metodami bo vsebovan v (glavni) datoteki dama.py. Uporabljene metode bodo:
##* izbira_igralca(self)
##* zacni_igro(self)
##* premakni_figuro(self,i,j)
##* koncaj_igro(self, zmagovalec)
##


##
###### Razred Igra: <h4>
##Metode znotraj razreda Igra bodo:
##* naredi_potezo(self,i,j), ki se bo razdelila na podmetodi premakni(self,i,j) in pojej(self,i,j)
##* razveljavi(self)
##* na_potezi(self)
##* je_veljavna(self,i,j)
##* zmagovalec(self)



##class Figura():
##    def __init__(self, barva, dama = False, vrstica, stolpec):
##        self.barva = barva
##        
        


class Igra():
    def __init__(self):
        self.deska = [[C, False, C, False, C, False, C, False],
                      [False, C, False, C, False, C, False, C],
                      [C, False, C, False, C, False, C, False],
                      [False,None,False,None,False,None,False,None],
                      [None,False,None,False,None,False,None,False],
                      [False, B, False, B, False, B, False, B],
                      [B, False, B, False, B, False, B, False],
                      [False, B, False, B, False, B, False, B]]
        
        self.na_potezi = crni
        self.zgodovina = self.deska
        
    def shrani_potezo(self):
# seznamu zgodovina pripne par (trenutna pozicija na deski, igralec na potezi)
        self.zgodovina.append((self.deska, self.na_potezi))

    
    def razveljavi(self):
# ce igra clovek proti cloveku se razveljavi ena poteza, sicer pa dve(SE DODATI!!)
        (self.deska, self.na_potezi) = self.zgodovina.pop()

# pop odstrani zadnji element seznama

    def je_veljavna(self, i, j):
        for i in range(8):
            for j in range(8):
                if self.zgodovina[-1][i][j] == None:
                    return True
        return False

    
    def zmagovalec(self):
        pass
    
    def pojej(self, i, j):
        pass
    
    def premakni(self, i, j):
        pass
    
    def naredi_potezo(self, i, j):
    # če je poteza neveljavna ne naredi ničesar
        if not je_veljavna(self, i, j):
            return None
    # če je poteza veljavna jo izvede
        
##########################            

###### Igralci in njihovi razredi: <h4>
##Igra proti računalniku bo vsebovala dva algoritma, enega namerno neizpopolnjenega in lažjega (Minimax) in pa bolj dodelanega (alfa-beta rezanje). Tretja možnost je, da je igralec človek, v tem primeru mu podelimo možnost izvajanja poteze preko uporabniškega vmesnika. Razredi igralcev bodo:
##* class Minimax 
##* class Alfa_beta
##* class clovek, ki bo imel metodi:
##    * __init__(self, gui), ki se bo povezala z uporabniškim vmesnikom, 
##    * premakni(self)

class Clovek():
    def __init__(self, gui):
        self.gui = gui
    def premakni(self):
        pass

class Minimax():
    pass

class Alfa_Beta():
    pass
            
##########################


    







    

