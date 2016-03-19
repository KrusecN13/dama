##
###### Razred Igra: <h4>
##Metode znotraj razreda Igra bodo:
##* naredi_potezo(self,i,j), ki se bo razdelila na podmetodi premakni(self,i,j) in pojej(self,i,j)
##* razveljavi(self)
##* na_potezi(self)
##* je_veljavna(self,i,j)
##* zmagovalec(self)


NI_KONEC = "ni konec"


class Figura():
    def __init__(self, igralec, dama = False):
        self.igralec = igralec
        self.dama = dama
    #def __repr__
        
        
def nasprotnik(igralec):
    if igralec == igrC:
        return igrB
    elif igralec == igrB:
        return igrC
    else:
        assert False
    


class Igra():
    def __init__(self):

        # None spremeniti v gui ko bo definirano
        igrC = Clovek(None,1)
        igrB = Clovek(None,-1)
        self.deska = [[Figura(igrC), False, Figura(igrC), False, Figura(igrC), False, Figura(igrC), False],
                      [False, Figura(igrC), False, Figura(igrC), False, Figura(igrC), False, Figura(igrC)],
                      [Figura(igrC), False, Figura(igrC), False, Figura(igrC), False, Figura(igrC), False],
                      [False,None,False,None,False,None,False,None],
                      [None,False,None,False,None,False,None,False],
                      [False, Figura(igrB), False, Figura(igrB),False, Figura(igrB), False, Figura(igrB)],
                      [Figura(igrB), False, Figura(igrB), False, Figura(igrB), False, Figura(igrB), False],
                      [False, Figura(igrB), False, Figura(igrB),False, Figura(igrB), False, Figura(igrB)]]
        
        
        self.na_potezi = igrC
        self.zgodovina = [(self.deska, igrC)]

##        self.figure = []
##        for i in range(8):
##            for j in range(8):
##                if self.deska[i][j] is not None and not False:
##                    self.figure.append(self.deska[i][j])


        
    
    def shrani_potezo(self):
# seznamu zgodovina pripne par (trenutna pozicija na deski, igralec na potezi)
        a = [self.deska[j][:] for j in range(8)]
        self.zgodovina.append((a, self.na_potezi))
        

    def kopija(self):
        kopy = Igra()
        kopy.deska = [self.deska[j][:] for j in range(8)]
        kopy.na_potezi = self.na_potezi
        return kopy

    def veljavne_poteze(self, igr):
        premakni = []
        pojej = []
        for i in range(8):
            for j in range(8):
                if self.deska[i][j].igralec == igr :
                    if 0 <= (i-2) <= 7 and 0 <= (j+2*igr.smer) <= 7 and self.deska[i-2][j+2*igr.smer] == None and self.deska[i-1][j+1*igr.smer] == Figura(nasprotnik(igr)):
                        pojej.append((i,j), (i-2, j+2*igr.smer))
                    if 0 <= (i+2) <= 7 and 0 <= (j+2*igr.smer) <= 7 and self.deska[i+2][j+2*igr.smer] == None and self.deska[i+1][j+1*igr.smer] == Figura(nasprotnik(igr)):
                        pojej.append((i,j), (i+2, j+2*igr.smer))
                    
                    if 0 <= (i-1) <= 7 and 0 <= (j+1*igr.smer) <= 7 and self.deska[i-1][j+1*igr.smer] == None:
                        premakni.append((i,j), (i-1, j+1*igr.smer))
                    if 0 <= (i+1) <= 7 and 0 <= (j+1*igr.smer) <= 7 and self.deska[i+1][j+1*igr.smer] == None:
                        premakni.append((i,j), (i+1, j+1*igr.smer))
            
        return (pojej, premakni)
                    
                    
  
    
    def stanje(self):
        # ugotovi, ali že imamo zmagovalca in ga vrne, oz. sporoèi da še ni konec igre
        (pojej, premakni) = veljavne_poteze(nasprotnik(igr))
        if pojej == [] and premakni ==[]:
            return self.na_potezi
        else:
            return (NI_KONEC)
        
                   
    
    def naredi_potezo(self,p,r):
    # če je poteza neveljavna ne naredi ničesar
    # če je poteza veljavna jo izvede
    # p so stare koordinate(kjer figura stoji), r so nove(kamor se hoèe premakniti)
        (p1,p2) = p
        (r1, r2) = r
        (pojej, premakni) = veljavne_poteze(igr)
        for i in pojej:
            if (p,r) == i:
                self.shrani_potezo()
                self.deska[r1][r2] = self.deska[p1][p2]
                self.deska[p1][p2] = None
                self.deska[(p1+r1)/2][(p2+r2)/2] = None
                zmagovalec = self.stanje()
                
                if r1 == 0 or r1 == 7:
                    self.deska[r1][r2].dama = True
                        
                        
                if zmagovalec == NI_KONEC:
                    self.na_potezi = nasprotnik(self.na_potezi)
                else:
                    self.na_potezi = None
                    return zmagovalec
        for j in premakni:
            if (p,r) == i:
                self.shrani_potezo()
                self.deska[r1][r2] = self.deska[p1][p2]
                self.deska[p1][p2] = None
                zmagovalec = self.stanje()
                
                if r1 == 0 or r1 == 7:
                    self.deska[r1][r2].dama = True
                    
                if zmagovalec == NI_KONEC:
                    self.na_potezi = nasprotnik(self.na_potezi)
                else:
                    self.na_potezi = None
                    return zmagovalec
        return None
                 
                               

                                                                                                                                                                  
                                                                                                                                                          


                                                                                                                                                          


        
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
    def __init__(self, gui, smer):
        self.gui = gui
        self.smer = smer
    def premakni(self):
        pass

class Minimax():
    pass

class Alfa_Beta():
    pass
            
##########################











    

