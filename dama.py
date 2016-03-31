import threading
import logging

# -*- coding: cp1250 -*-
##
###### Razred Igra: <h4>
##Metode znotraj razreda Igra bodo:
##* naredi_potezo(self,i,j), ki se bo razdelila na podmetodi premakni(self,i,j) in pojej(self,i,j)
##* razveljavi(self)
##* na_potezi(self)
##* je_veljavna(self,i,j)
##* zmagovalec(self)

CRNI = 'CRNI'
BELI = 'BELI'
        
NI_KONEC = "ni konec"
GLOBINA = 3

class Clovek():
    def __init__(self, gui):
        self.gui = gui
        
    def igraj(self):
        pass

    def prekini(self):
        pass

    def klik(self,p):
        print('to je ze v kliku', p)
        self.gui.naredi_potezo(p[0], p[1])
        print ("Clovek je naredil potezo {0}".format(p))

class Racunalnik():
    def __init__(self, gui, algoritem):
        self.gui = gui
        self.algoritem = Minimax(3)
        self.vlakno = None

    def igraj(self):
    # vzporedno vlakno ki najde najbolso potezo
        self.vlakno = threading.Thread(
            target = lambda: self.algoritem.najdi_potezo(self.gui.igra.kopija()))
        

        self.vlakno.start()

        #vsake 100ms preveri, ali je bila najdena poteza
        self.gui.kanvas.after(100, self.preveri)

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

    def klik(self,a, p):
        #ker igra racunalnik se ne odzove na klike
        pass           
        


class Figura():
    def __init__(self, igralec, dama = False, indeks = False):
        self.igralec = igralec
        self.dama = dama
        self.indeks = indeks
        
    def __repr__(self):
        return 'Figura(%s, %s, %s)' % (self.igralec, self.dama, self.indeks)

    
def nasprotnik(igralec):
    if igralec == CRNI:
        return BELI
    elif igralec == BELI:
        return CRNI
    else:
        assert False
    


class Igra():
    def __init__(self):

        self.deska = [[Figura(CRNI), False, Figura(CRNI), False, Figura(CRNI), False, Figura(CRNI), False],
                      [False, Figura(CRNI), False, Figura(CRNI), False, Figura(CRNI), False, Figura(CRNI)],
                      [Figura(CRNI), False, Figura(CRNI), False, Figura(CRNI), False, Figura(CRNI), False],
                      [False,None,False,None,False,None,False,None],
                      [None,False,None,False,None,False,None,False],
                      [False, Figura(BELI), False, Figura(BELI),False, Figura(BELI), False, Figura(BELI)],
                      [Figura(BELI), False, Figura(BELI), False, Figura(BELI), False, Figura(BELI), False],
                      [False, Figura(BELI), False, Figura(BELI),False, Figura(BELI), False, Figura(BELI)]]
        
        
        self.na_potezi = CRNI
        self.zgodovina = [(self.deska, CRNI)]

        print(self.na_potezi)
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
        # igr pomeni igralca
        smer = (1 if igr == CRNI else -1)
        premakni = []
        pojej = []
        for i in range(8):
            for j in range(8):
                if self.deska[j][i] != False and self.deska[j][i] != None:
                    if self.deska[j][i].igralec == igr :
                        if 0 <= (i-2) <= 7 and 0 <= (j+2*smer) <= 7 and self.deska[j+2*smer][i-2] == None and self.deska[j+1*smer][i-1] == Figura(nasprotnik(igr)):
                            pojej.append(((i,j), (i-2, j+2*smer)))
                        if 0 <= (i+2) <= 7 and 0 <= (j+2*smer) <= 7 and self.deska[j+2*smer][i+2] == None and self.deska[j+1*smer][i+1] == Figura(nasprotnik(igr)):
                            pojej.append(((i,j), (i+2, j+2*smer)))
                    
                        if 0 <= (i-1) <= 7 and 0 <= (j+1*smer) <= 7 and self.deska[j+1*smer][i-1] == None:
                            premakni.append(((i,j), (i-1, j+1*smer)))
                        if 0 <= (i+1) <= 7 and 0 <= (j+1*smer) <= 7 and self.deska[j+1*smer][i+1] == None:
                            premakni.append(((i,j), (i+1, j+1*smer)))
        
        return (pojej, premakni)
                    
                    
  
    
    def stanje(self):
        
        # ugotovi, ali ce imamo zmagovalca in ga vrne, oz. sporoci da ce ni konec igre
        (pojej, premakni) = self.veljavne_poteze(nasprotnik(self.na_potezi))
        if pojej == [] and premakni ==[]:
            return self.na_potezi
        else:
            return (NI_KONEC)
        
                   
    
    def naredi_potezo(self,p,r):
    # ce je poteza neveljavna ne naredi nicesar
    # ce je poteza veljavna jo izvede
    # p so stare koordinate(kjer figura stoji), r so nove(kamor se hoce premakniti)
        (p1,p2) = p
        (r1,r2) = r
        (pojej, premakni) = self.veljavne_poteze(self.na_potezi)
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
            if (p,r) == j:
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
##Igra proti racunalniku bo vsebovala dva algoritma, enega namerno neizpopolnjenega in lazjega (Minimax)
##in pa bolj dodelanega (alfa-beta rezanje). Tretja moznost je, da je igralec clovek, v tem primeru mu podelimo#
##moznost izvajanja poteze preko uporabniskega vmesnika. Razredi igralcev bodo:
##* class Minimax 
##* class Alfa_beta
##* class clovek, ki bo imel metodi:
##    * __init__(self, gui), ki se bo povezala z uporabniskim vmesnikom, 
##    * premakni(self)
class Minimax():
    def __init__(self, globina):
        self.globina = GLOBINA
        self.prekinitev = False
        self.igra = None
        self.jaz = None
        self.poteza = None
#        self.vrednost = None
        
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


    ZMAGA = 10000000
    NESKONCNO = ZMAGA + 100
    vrednost_st_figur = 300
    vrednost_st_premikov = 100
    vrednost_st_pojej = 200
    
    def vrednost_polja(self):
        st_figur = 0
        for i in range(8):
            for j in range(8):
                if self.igra.deska[j][i] == Figura(self.igra.na_potezi):
                    st_figur += 1

        (pojej, premakni) = self.igra.veljavne_poteze(self.igra.na_potezi)
        st_pojej = len(pojej)
        st_premikov = len(premakni)
#        self.vrednost = vrednost_st_figur * st_figur + vrednost_st_premikov * st_premikov + vrednost_st_pojej * st_pojej
        return (vrednost_st_figur * st_figur + vrednost_st_premikov * st_premikov + vrednost_st_pojej * st_pojej)


        

    
    def minimax(self, globina, maksimiziramo):
         
        if self.prekinitev:
            logging.debug ("Minimax prekinja, globina = {0}".format(self.globina))
            return (None,0)
        (zmagovalec) = self.igra.stanje()
        if zmagovalec in (CRNI,BELI):
            if zmagovalec == self.jaz:
                return (None, Minimax.ZMAGA)
            elif zmagovalec == nasprotnik(self.jaz):
                return (None, -Minimax.ZMAGA)
        elif zmagovalec == NI_KONEC:
            if self.globina == 0:
                return (None, self.vrednost_polja())
            else:
                if maksimiziramo:
                    sez = self.igra.veljavne_poteze(self.jaz)[0]
                    if sez == []:
                        sez = self.igra.veljavne_poteze(self.jaz)[1]
                    najboljsa_poteza = None
                    vrednost_najboljse = -Minimax.NESKONCNO
                    for (p1,p2) in sez:
                        self.igra.naredi_potezo(p1,p2)
                        vrednost = self.minimax(self.globina-1, not maksimiziramo)[1]
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
                        self.igra.naredi_potezo(p1,p2)
                        vrednost = self.minimax(self.globina-1, not maksimiziramo)[1]
                        self.igra.razveljavi()
                        if vrednost < vrednost_najboljse:
                            vrednost_najboljse = vrednost
                            najboljsa_poteza = (p1,p2)

                assert (najboljsa_poteza is not None), "minimax: izracunana poteza je None"
                return (najboljsa_poteza, vrednost_najboljse)
        else:
            assert False, "minimax: nedefinirano stanje igre "
            
                        
            
                          

class Alfa_Beta():
    pass
            



print(Igra().veljavne_poteze(CRNI))








    

