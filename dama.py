import threading
import logging

##
###### Razred Igra: <h4>
##Metode znotraj razreda Igra bodo:
##* naredi_potezo(self,i,j), ki se bo razdelila na podmetodi premakni(self,i,j) in pojej(self,i,j)
##* razveljavi(self)
##* na_potezi(self)
##* je_veljavna(self,i,j)
##* zmagovalec(self)


NI_KONEC = "ni konec"
GLOBINA = 3

class Figura():
    def __init__(self, igralec, dama = False):
        self.igralec = igralec
        self.dama = dama
    def __repr__(self):
        return 'Figura(%s, %s)' % (self.igralec, self.dama)

        
        
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

    
    def shrani_potezo(self):
# seznamu zgodovina pripne par (trenutna pozicija na deski, igralec na potezi)
        a = [self.deska[j][:] for j in range(8)]
        self.zgodovina.append((a, self.na_potezi))
        

    def kopija(self):
        kopy = Igra()
        kopy.deska = [self.deska[j][:] for j in range(8)]
        kopy.na_potezi = self.na_potezi
        return kopy
    
    def razveljavi(self):
        (self.deska,self.na_potezi) = self.zgodovina.pop()

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
        
    def igraj(self):
        pass

    def prekini(self):
        pass

    def klik(self,p):
        self.gui.naredi_potezo(a,p)

class Racunalnik():
    def __init__(self, gui, algoritem):
        self.gui = gui
        self.algoritem = algoritem
        self.vlakno = None

    def igraj(self):
    # vzporedno vlakno ki najde najbolso potezo
        self.vlakno = threading.Thread(
            target = lambda: self.algoritem.najdi_potezo(self.gui.igra.kopija()))
        

        self.vlakno.start()

        #vsake 100ms preveri, ali je bila najdena poteza
        self.gui.deska.after(100, self.preveri)

    def preveri(self):
        if self.algoritem.poteza is not None:
            self.gui.naredi_potezo(a,self.algoritem.poteza)
            self.vlakno = None
        else:
            self.gui.deska.after(100, self.preveri)

    def prekini(self):
        if self.vlakno:
            logging.debug("Prekini {0}".format(self.vlakno))
            self.algoritem.prekini()
            self.vlakno.join()
            self.vlakno = None

    def klik(self,p):
        #ker igra racunalnik se ne odzove na klike
        pass           
        


        

class Minimax():
    def __init__(self, globina):
        self.globina = globina
        self.prekinitev = False
        self.igra = None
        self.jaz = None
        self.poteza = None
        
    def prekini(self):
        self.prekinitev = True
        
    def najdi_potezo(self,igra):
        self.igra = igra
        self.prekinitev = False
        self.jaz = self.igra.na_potezi
        self.poteza = None
        (poteza,vrednost) = self.minimax(self.globina,True)
        self.jaz = None
        self.igra = None
        if not self.prekinitev:
            logging.debug("minimax: poteza {0}, vrednost {1}".format(poteza, vrednost))
            self.poteza = poteza


    ZMAGA = 100000
    NESKONCNO = ZMAGA + 100
    def vrednost_polja(self):

    #najprej lociva pojej in premakni z funkcijo, potem ustvariva slovar, in vsakem kljucu, ki
    #bojo par iz tega seznama, prirediva vrednost, glede na napisano hevristiko.
    #na koncu napiševa funkcijo, ki gre èez cel slovar in poišce najboljso vrednost
        sez = []
        pass
        
    
    def minimax(self, globina, maksimiziramo):
        if self.prekinitev:
            logging.debug ("Minimax prekinja, globina = {0}".format(globina))
            return (None,0)
        (zmagovalec) = self.igra.stanje()
        if zmagovalec in (igrC,IgrB):
            if zmagovalec == self.jaz:
                return (None, Minimax.ZMAGA)
            elif zmagovalec == nasprotnik(self.jaz):
                return (None, -Minimax.ZMAGA)
        elif zmagovalec == NI_KONEC:
            if globina == 0:
                return (None, self.vrednost_polja())
            else:
                if maksimiziramo:
                    sez = self.igra.veljavne_poteze(self.jaz)[0]
                    if sez == []:
                        sez = self.igra.veljavne_poteze(self.jaz)[1]
                    najboljsa_poteza = None
                    vrednost_najboljse = -Minimax.NESKONCNO
                    for (p1,p2) in sez:
                        self.igra.naredi_potezo((p1,p2))
                        vrednost = self.minimax(globina-1, not maksimiziramo)[1]
                        self.igra.razveljavi()
                        if vrednost > vrednost_najboljse:
                            vrednost_najboljse = vrednost
                            najboljsa_poteza = (p1,p2)
                else:
                    sez = self.igra.veljavne_poteze(self.jaz)[0]
                    najboljsa_poteza = None
                    vrednost_najboljse = Minimax.NESKONCNO
                    if sez == []:
                        sez = self.igra.veljavne_poteze(self.jaz)[1]
                    for (p1,p2) in sez:
                        self.igra.naredi_potezo((p1,p2))
                        vrednost = self.minimax(globina-1, not maksimiziramo)[1]
                        self.igra.razveljavi()
                        if vrednost < vrednost_najboljse:
                            vrednost_najboljse = vrednost
                            najboljsa_poteza = (p1,p2)

                assert (najboljsa_poteza is not None), "minimax: izracunana poteza je None"
                return (najboljsa_poteza, vrednost_najboljse)
        else:
            assert False, "minimax: nedefinirano stanje igre"
            
                        
            
                          

class Alfa_Beta():
    pass
            












    

