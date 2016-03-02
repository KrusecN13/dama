###### Razred GUI: <h4>
##Vmesnik bo vseboval metode, s katerimi bo risal poteze na platno. Celotni razred skupaj z metodami bo vsebovan v (glavni) datoteki dama.py. Uporabljene metode bodo:
##* izbira_igralca(self)
##* zacni_igro(self)
##* premakni_figuro(self,i,j)
##* koncaj_igro(self, zmagovalec)
##
###### Igralci in njihovi razredi: <h4>
##Igra proti računalniku bo vsebovala dva algoritma, enega namerno neizpopolnjenega in lažjega (Minimax) in pa bolj dodelanega (alfa-beta rezanje). Tretja možnost je, da je igralec človek, v tem primeru mu podelimo možnost izvajanja poteze preko uporabniškega vmesnika. Razredi igralcev bodo:
##* class Minimax 
##* class Alfa_beta
##* class clovek, ki bo imel metodi:
##    * __init__(self, gui), ki se bo povezala z uporabniškim vmesnikom, 
##    * premakni(self)
##
###### Razred Igra: <h4>
##Metode znotraj razreda Igra bodo:
##* naredi_potezo(self,i,j), ki se bo razdelila na podmetodi premakni(self,i,j) in pojej(self,i,j)
##* razveljavi(self)
##* na_potezi(self)
##* je_veljavna(self,i,j)
##* zmagovalec(self)

class Igra():
    def __init__(self):
        self.deska = [[C, None, C, None, C, None, C, None],
                      [None, C, None, C, None, C, None, C],
                      [C, None, C, None, C, None, C, None],
                      [None,None,None,None,None,None,None,None]
                      [None,None,None,None,None,None,None,None]
                      [B, None, B, None, B, None, B, None]
                      [None, B, None, B, None, B, None, B]
                      [B, None, B, None, B, None, B, None]]
    def shrani_potezo(self):
        pass
    def razveljavi(self):
        pass

    def je_veljavna(self, i, j):
        pass
    def zmagovalec(self):
        pass
    def naredi_potezo(self, i, j):
        pass
    







    

