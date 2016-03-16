##
###### Razred Igra: <h4>
##Metode znotraj razreda Igra bodo:
##* naredi_potezo(self,i,j), ki se bo razdelila na podmetodi premakni(self,i,j) in pojej(self,i,j)
##* razveljavi(self)
##* na_potezi(self)
##* je_veljavna(self,i,j)
##* zmagovalec(self)

igralec_C = "crna"
igralec_B = "bela"
NI_KONEC = "ni konec"


class Figura():
    def __init__(self, barva, dama = False):
        self.barva = (crna or bela)
        self.dama = dama
        
        
def nasprotnik(igralec):
    if igralec == igralec_C:
        return igralec_B
    elif igralec == igralec_B:
        return igralec_C
    else:
        assert False
    


class Igra():
    def __init__(self):
        self.deska = [[Figura(crna), False, Figura(crna), False, Figura(crna), False, Figura(crna), False],
                      [False, Figura(crna), False, Figura(crna), False, Figura(crna), False, Figura(crna)],
                      [Figura(crna), False, Figura(crna), False, Figura(crna), False, Figura(crna), False],
                      [False,None,False,None,False,None,False,None],
                      [None,False,None,False,None,False,None,False],
                      [False, Figura(bela), False, Figura(bela),False, Figura(bela), False, Figura(bela)],
                      [Figura(bela), False, Figura(bela), False, Figura(bela), False, Figura(bela), False],
                      [False, Figura(bela), False, Figura(bela),False, Figura(bela), False, Figura(bela)]]
        
        
        self.na_potezi = igralec_C
        self.zgodovina = [(self.deska, igralec_C)]

        self.figure = []
        for i in range(8):
            for j in range(8):
                if self.deska[i][j] is not None and not False:
                    self.figure.append(self.deska[i][j])
        print(self.figure)
                    




        
    
    def shrani_potezo(self):
# seznamu zgodovina pripne par (trenutna pozicija na deski, igralec na potezi)
        a = [self.deska[j][:] for j in range(8)]
        self.zgodovina.append((a, self.na_potezi))
        

    
    def razveljavi(self):
# ce igra clovek proti cloveku se razveljavi ena poteza, sicer pa dve(SE DODATI!!)
        (self.deska, self.na_potezi) = self.zgodovina.pop()
##??? ali ta funkcija ze avtomatsko vzame zadnji element 'nove' zgodovine?
##?? ali celoten seznam zgodovine


# pop odstrani zadnji element seznama

    def kopija(self):
        kopy = Igra()
        kopy.deska = [self.deska[j][:] for j in range(8)]
        kopy.na_potezi = self.na_potezi
        return kopy

    def veljavne_poteze(self, figura):
        premakni = []
        pojej = []
        figura = Figura(barva)
        for i in range(8):
            for j in range(8):
                if figura.barva == crna :
                    if 0 <= (i-2) <= 7 and 0 <= (j+2) <= 7 and self.deska[i-2][j+2] == None and self.deska[i-1][j+1] == Figura(bela):
                        pojej.append((i,j), (i-2, j+2))
                    if 0 <= (i+2) <= 7 and 0 <= (j+2) <= 7 and self.deska[i+2][j+2] == None and self.deska[i+1][j+1] == Figura(bela):
                        pojej.append((i,j), (i+2, j+2))
                    
                    if 0 <= (i-1) <= 7 and 0 <= (j+1) <= 7 and self.deska[i-1][j+1] == None:
                        premakni.append((i,j), (i-1, j+1))
                    if 0 <= (i+1) <= 7 and 0 <= (j+1) <= 7 and self.deska[i+1][j+1] == None:
                        premakni.append((i,j), (i+1, j+1))
                        
                if figura.barva == bela :
                    if 0 <= (i-2) <= 7 and 0 <= (j-2) <= 7 and self.deska[i-2][j-2] == None and self.deska[i-1][j-1] == Figura(bela):
                        pojej.append((i,j), (i-2, j-2))
                    if 0 <= (i+2) <= 7 and 0 <= (j-2) <= 7 and self.deska[i+2][j-2] == None and self.deska[i+1][j-1] == Figura(bela):
                        pojej.append((i,j), (i+2, j-2))
                    
                    if 0 <= (i-1) <= 7 and 0 <= (j-1) <= 7 and self.deska[i-1][j-1] == None:
                        premakni.append((i,j), (i-1, j-1))
                    if 0 <= (i+1) <= 7 and 0 <= (j-1) <= 7 and self.deska[i+1][j-1] == None:
                        premakni.append((i,j), (i+1, j-1))
        return (pojej, premakni)
                    
                    
  
    
    def stanje(self):
        # ugotovi, ali že imamo zmagovalca in ga vrne, oz.
       
        if veljavne_poteze() == ([],[]):
            return nasprotnik(self.na_potezi)
        else:
            return (NI_KONEC)
        
                   
    
    def naredi_potezo(self,figura):
    # če je poteza neveljavna ne naredi ničesar
    # če je poteza veljavna jo izvede
        
        
        
        
    





##k = Igra()
##k.figure


        
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











    

