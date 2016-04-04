import threading # za vzporedno izvajanje vlaken
import logging   # za odpravljanje napak
from random import *

CRNI = 'CRNI'
BELI = 'BELI'
NEVELJAVNO = 'NEVELJAVNO'
        
NI_KONEC = "ni konec"

###########################################
## Razred Clovek za igranje uporabnika:
###########################################

class Clovek():
    def __init__(self, gui):
        self.gui = gui
        
    def igraj(self):
        # Čakamo, da uporabnik klikne na ploščo, na kar nas
        # opozori Gui preko metode kanvas_klika
        pass

    def prekini(self):
        # Metoda za prekinitev razmišljanja, ki jo človek ignorira
        pass

    def klik(self,p):
        # Naredimo potezo, če je veljavna
        self.gui.naredi_potezo(p[0], p[1])
        

###############################################
## Razred Racunalnik za igranje racunalnika:
###############################################
        
class Racunalnik():
    def __init__(self, gui, algoritem):
        self.gui = gui
        self.algoritem = algoritem
        self.vlakno = None

    def igraj(self):
        # Vzporedno vlakno ki najde najboljso potezo na kopiji igre, da se Gui ne zmede.
        # Glavno vlakno, ki uporablja tkinter, preverja ali je bila poteza že
        # najdena (s pomočjo metode preveri).
        self.vlakno = threading.Thread(
            target=lambda: self.algoritem.najdi_potezo(self.gui.igra.kopija()))
        # Vlakno začne delati
        self.vlakno.start()

        # Vsake 100ms preveri, ali je bila poteza že najdena.
        self.gui.kanvas.after(100, self.preveri)

    def preveri(self):
        if self.algoritem.poteza is not None:
            # Če je algoritem že najdel potezo jo naredi in vlakno ponastavimo.
            self.gui.naredi_potezo(self.algoritem.poteza[0],self.algoritem.poteza[1])
            self.vlakno = None
        else:
            # Če algoritem še ni najdel poteze, preveri še enkrat čez 100ms.
            self.gui.kanvas.after(100, self.preveri)

    def prekini(self):
        # Gui kliče to metodo, če je potrebno prekiniti razmisljanje.
        if self.vlakno:
            # Algoritmu sporocimo, da preneha z razmišljanjem in
            # pocakamo, da se ustavi.
            logging.debug("Prekini {0}".format(self.vlakno))
            self.algoritem.prekini()
            self.vlakno.join()
            self.vlakno = None

    def klik(self,p):
        #Ker igra racunalnik se ne odzove na klike!
        pass           
        
############################################################
## Razred Figura, kjer imamo shranjene vse figure na deski:
############################################################

class Figura():
    def __init__(self, igralec, dama = False, indeks = False):
        self.igralec = igralec
        self.dama = dama
        self.indeks = indeks
        
    def __repr__(self):
        # Metoda za izpis objekta razreda Figura.
        return 'Figura(%s, %s, %s)' % (self.igralec, self.dama, self.indeks)

    def kopija(self):
        return Figura(self.igralec, dama=self.dama, indeks=self.indeks)


##########################
## Razred Igra:
##########################
    
def nasprotnik(igralec):
    # Vrne nasprotnika od igralca
    if igralec == CRNI:
        return BELI
    elif igralec == BELI:
        return CRNI
    else:
        # Imamo le dva igralca, zato se ta možnost ne sme zgoditi.
        # Če se zgodi, je nekje napaka in program se prekine.
        assert False, "Neveljaven nasprotnik: {0}".format(igralec)
    


class Igra():
    def __init__(self):

        self.deska = [[Figura(CRNI), NEVELJAVNO, Figura(CRNI), NEVELJAVNO, Figura(CRNI), NEVELJAVNO, Figura(CRNI), NEVELJAVNO],
                      [NEVELJAVNO, Figura(CRNI), NEVELJAVNO, Figura(CRNI), NEVELJAVNO, Figura(CRNI), NEVELJAVNO, Figura(CRNI)],
                      [Figura(CRNI), NEVELJAVNO, Figura(CRNI), NEVELJAVNO, Figura(CRNI), NEVELJAVNO, Figura(CRNI), NEVELJAVNO],
                      [NEVELJAVNO,None,NEVELJAVNO,None,NEVELJAVNO,None,NEVELJAVNO,None],
                      [None,NEVELJAVNO,None,NEVELJAVNO,None,NEVELJAVNO,None,NEVELJAVNO],
                      [NEVELJAVNO, Figura(BELI), NEVELJAVNO, Figura(BELI),NEVELJAVNO, Figura(BELI), NEVELJAVNO, Figura(BELI)],
                      [Figura(BELI), NEVELJAVNO, Figura(BELI), NEVELJAVNO, Figura(BELI), NEVELJAVNO, Figura(BELI), NEVELJAVNO],
                      [NEVELJAVNO, Figura(BELI), NEVELJAVNO, Figura(BELI),NEVELJAVNO, Figura(BELI), NEVELJAVNO, Figura(BELI)]]
        
        
        self.na_potezi = CRNI
        self.zgodovina = [(self.deska, CRNI)]


    def kopija_figure(self, j, i):
        fig = self.deska[j][i] 
        if fig == NEVELJAVNO or fig == None:
            return fig
        else:
            return self.deska[j][i].kopija()

    def kopija_deske(self):
        return [[self.kopija_figure(j,i) for i in range(8)] for j in range(8)]

    def shrani_potezo(self):
        # Seznamu zgodovina pripne par (trenutna pozicija na deski, igralec na potezi).
        # Potezo shranimo da lahko kličemo metodo razveljavi
        a = self.kopija_deske()
        self.zgodovina.append((a, self.na_potezi))
      
        
    def kopija(self):
        # Vrne kopijo igre, ki jo uporabimo pri razmišljanju algoritma.
        # Ko algoritem razmišlja vnaprej, bi se Gui zmedel, saj bi se
        # nenehno menjavalo stanje igre.
        kopy = Igra()
        kopy.deska = self.kopija_deske()
        kopy.na_potezi = self.na_potezi
        return kopy
    
    def razveljavi(self):
        # Razveljavi potezo.
        (self.deska,self.na_potezi) = self.zgodovina.pop()
       

    def veljavne_poteze(self, igr):
        # Argument igr pomeni igralca, za katerega nas zanimajo veljavne poteze

        # Vrne seznama vseh veljavnih potez za enega igralca, kjer je prvi
        # seznam pojej seznam vseh potez, ki odvzamejo nasprotniku figuro.
        # Drugi seznam je seznam vseh možnih premikov.
        smer = (1 if igr == CRNI else -1)
        # S smerjo je definirana smer, v kateri se premika igralec.
        # Črni igralec se premika dol, beli pa gor.
        
        premakni = []
        pojej = []
        for j in range(8):
            for i in range(8):
                # Pregledamo desko, gremo po vseh figurah.
                if self.deska[j][i] != NEVELJAVNO and self.deska[j][i] != None:
                    # Preverimo, kateremu igralcu pripada figura na (j,i) mestu na deski.
                    if self.deska[j][i].igralec == igr :
                        # Ločimo primera, če je figura dama ali ne.
                        # Če je dama, potem se lahko premika v vse smeri.
                        if self.deska[j][i].dama:
                            # v naslednjih if-stavkih preverimo:
                                #1. da i in j ne padeta ven iz polja, 
                                #2. če je polje kamor premikamo figuro prazno,
                                #3. pri odvzemu nasprotnikove figure preverimo, če je na ustreznem
                                # mestu nasprotnikova figura in diagonalno za njo prazno polje.
                                
                            # vse poteze dol
                            if 0 <= (i-2) <= 7 and 0 <= (j+2) <= 7 and self.deska[j+2][i-2] == None:
                                 if self.deska[j+1][i-1]:
                                     if self.deska[j+1][i-1].igralec == nasprotnik(self.na_potezi):
                                          pojej.append(((i,j), (i-2, j+2)))
                                          
                            if 0 <= (i+2) <= 7 and 0 <= (j+2) <= 7 and self.deska[j+2][i+2] == None:
                                 if self.deska[j+1][i+1]:
                                    if self.deska[j+1][i+1].igralec == nasprotnik(self.na_potezi):
                                         pojej.append(((i,j), (i+2, j+2)))
                                         
                            if 0 <= (i-1) <= 7 and 0 <= (j+1) <= 7 and self.deska[j+1][i-1] == None:
                                  premakni.append(((i,j),(i-1,j+1)))
                            if 0 <= (i+1) <= 7 and 0 <= (j+1) <= 7 and self.deska[j+1][i+1] == None:
                                    premakni.append(((i,j),(i+1,j+1)))

                            #vse poteze gor
                            if 0 <= (i-2) <= 7 and 0 <= (j-2) <= 7 and self.deska[j-2][i-2] == None:
                                 if self.deska[j-1][i-1]:
                                     if self.deska[j-1][i-1].igralec == nasprotnik(self.na_potezi):
                                          pojej.append(((i,j), (i-2, j-2)))
                                          
                            if 0 <= (i+2) <= 7 and 0 <= (j-2) <= 7 and self.deska[j-2][i+2] == None:
                                 if self.deska[j-1][i+1]:
                                    if self.deska[j-1][i+1].igralec == nasprotnik(self.na_potezi):
                                         pojej.append(((i,j), (i+2, j-2)))
                                         
                            if 0 <= (i-1) <= 7 and 0 <= (j-1) <= 7 and self.deska[j-1][i-1] == None:
                                  premakni.append(((i,j),(i-1,j-1)))
                            if 0 <= (i+1) <= 7 and 0 <= (j-1) <= 7 and self.deska[j-1][i+1] == None:
                                    premakni.append(((i,j),(i+1,j-1)))
                        else:
                            # če figura ni dama, se premika le dol (črni) in gor (beli).
                            if 0 <= (i-2) <= 7 and 0 <= (j+2*smer) <= 7 and self.deska[j+2*smer][i-2] == None:
                                 if self.deska[j+1*smer][i-1]:
                                     if self.deska[j+1*smer][i-1].igralec == nasprotnik(self.na_potezi):
                                          pojej.append(((i,j), (i-2, j+2*smer)))
                            if 0 <= (i+2) <= 7 and 0 <= (j+2*smer) <= 7 and self.deska[j+2*smer][i+2] == None:
                                 if self.deska[j+1*smer][i+1]:
                                    if self.deska[j+1*smer][i+1].igralec == nasprotnik(self.na_potezi):
                                         pojej.append(((i,j), (i+2, j+2*smer)))
                            if 0 <= (i-1) <= 7 and 0 <= (j+1*smer) <= 7 and self.deska[j+1*smer][i-1] == None:
                                  premakni.append(((i,j),(i-1,j+1*smer)))
                            if 0 <= (i+1) <= 7 and 0 <= (j+1*smer) <= 7 and self.deska[j+1*smer][i+1] == None:
                                    premakni.append(((i,j),(i+1,j+1*smer)))
        return (pojej, premakni)
                    
    
    def stanje(self):
        # Ugotovi če imamo zmagovalca in ga vrne, oz. sporoči da igre še ni konec.
        (pojej, premakni) = self.veljavne_poteze(self.na_potezi)
        if pojej == [] and premakni ==[]:
            return nasprotnik(self.na_potezi)
        else:
            return (NI_KONEC)
        
                   
    
    def naredi_potezo(self,p,r):
    # Poteza mora biti veljavna
    
    # V argumentu p so podane stare koordinate (kjer figura stoji),
    # r pa so nove koordinate (kamor se hoče premakniti).
        self.shrani_potezo()
        (p1,p2) = p
        (r1,r2) = r
        (pojej, premakni) = self.veljavne_poteze(self.na_potezi)

        if abs (p1 - r1) == 1 and abs (p2 - r2) == 1:
            # Se premikamo
            self.deska[r2][r1] = self.deska[p2][p1]
            self.deska[p2][p1] = None
        elif abs (p1 - r1) == 2 and abs (p2 - r2) == 2:
            # Jemljemo
            self.deska[r2][r1] = self.deska[p2][p1]
            self.deska[p2][p1] = None
            b = (r2 + p2) // 2
            a = (r1 + p1) // 2
            self.deska[b][a] = None
        else:
            assert False, "neveljavna poteza {0}".format((p,r))
        # Spremnimo ga v damo, če je treba
        zeton = self.deska[r2][r1]
        zeton.dama = (zeton.igralec == CRNI and r2 == 7) or (zeton.igralec == BELI and r2 == 0)
        # Spremenimo, kdo je na potezi, če ni konec
        if self.stanje() == NI_KONEC:
            self.na_potezi = nasprotnik(self.na_potezi)
 
        
#############################################################            
## Razred Minimax:
#############################################################

class Minimax():
    #Ta razred uporablja algoritem minimax, s pomočjo katerega
    # računalnik razmišlja.
    # Nima dostopa do glavnega vlakna, ki uporablja Gui,
    # saj deluje v vzporednem vlaknu.
    
    def __init__(self, globina):
        self.globina = globina # Iščemo potezo glede na podano globino
        self.prekinitev = False # Če je prišlo do prekinitve.
        self.igra = None # Objekt, ki opisuje igro.
        self.jaz = None # Igralec katerega igramo.
        self.poteza = None # Najboljša najdena poteza.

        
    def prekini(self):
        # Če je uporabnik prekinil igro sporočimo vlaknu, naj
        # preneha razmišljati.
        self.prekinitev = True
        
    def najdi_potezo(self,igra):
        # Najde najboljšo potezo v trenutnem stanju igre.
        self.igra = igra
        self.prekinitev = False
        self.jaz = self.igra.na_potezi
        self.poteza = None
        # Algoritem minimax nam najde potezo.
        (poteza,vrednost) = self.minimax(self.globina,True)
        self.jaz = None
        self.igra = None
        if not self.prekinitev:
            logging.debug("minimax: poteza {0}, vrednost {1}".format(poteza, vrednost))
            self.poteza = poteza
        



    ZMAGA = 100000 #Vrednost zmage.
    NESKONCNO = ZMAGA + 100
    vrednost_dame = ZMAGA//10
    vrednost_st_figur = ZMAGA//100  
    vrednost_st_premikov = ZMAGA//1500
    vrednost_st_pojej = ZMAGA//1000


    def vrednost_polja(self):
        # Oceni vrednost polja, glede na število figur, ki jih še imamo,
        # glede na število možnih premikov in možnih odvzemov nasprotnikove
        # figure.
        st_figur = 0
        st_figur_naspr = 0
        dame = 0
        dame_naspr = 0
        for i in range(8):
            for j in range(8):
                if self.igra.deska[j][i] == Figura(self.igra.na_potezi):
                    st_figur += 1
                    if self.igra.deska[j][i].dama:
                        dame +=1
                elif self.igra.deska[j][i] == Figura(nasprotnik(self.igra.na_potezi)):
                    st_figur_naspr += 1
                    if self.igra.deska[j][i].dama:
                        dame_naspr += 1
                    
        (pojej1, premakni1) = self.igra.veljavne_poteze(self.igra.na_potezi)
        st_pojej1 = len(pojej1)
        st_premikov1 = len(premakni1)

        (pojej2, premakni2) = self.igra.veljavne_poteze(nasprotnik(self.igra.na_potezi))
        st_pojej2 = len(pojej2)
        st_premikov2 = len(premakni2)

        vrednost = (Minimax.vrednost_st_figur * st_figur + Minimax.vrednost_st_premikov * st_premikov1 + Minimax.vrednost_st_pojej * st_pojej1 + Minimax.vrednost_dame * dame - Minimax.vrednost_st_figur * st_figur_naspr - Minimax.vrednost_st_premikov * st_premikov2 - Minimax.vrednost_st_pojej * st_pojej2 - Minimax.vrednost_dame * dame_naspr)
        
        return vrednost



                
    
    def minimax(self, globina, maksimiziramo):
         
        if self.prekinitev:
            # Dobili smo sporočilo, da moramo prekiniti.
            logging.debug ("Minimax prekinja, globina = {0}".format(globina))
            return (None,0)
        
        zmagovalec = self.igra.stanje()
        if zmagovalec in (CRNI,BELI):
            # Če je igre konec, vrnemo njeno vrednost.
            if zmagovalec == self.jaz:
                return (None, Minimax.ZMAGA)
            elif zmagovalec == nasprotnik(self.jaz):
                return (None, -Minimax.ZMAGA)
            
        elif zmagovalec == NI_KONEC:
            self.preverjanje = True
            # Če igre še ni konec ločimo primera glede na globino.
            if globina == 0:
                return (None, self.vrednost_polja())
            else:


                if maksimiziramo:
                    # Maksimiziramo.
                    sez = self.igra.veljavne_poteze(self.jaz)[0]
                    if sez == []:
                        sez = self.igra.veljavne_poteze(self.jaz)[1]
                    najboljsa_poteza = None
                    vrednost_najboljse = -Minimax.NESKONCNO
                    # Poiščemo potezo z najboljšo vrednostjo.
                    for (p1,p2) in sez:
                 
                        self.igra.naredi_potezo(p1,p2)
                        vrednost = self.minimax(globina-1, not maksimiziramo)[1]
                        self.igra.razveljavi()
                        if vrednost > vrednost_najboljse:
                            vrednost_najboljse = vrednost
                            najboljsa_poteza = (p1,p2)
                else:
                    # Minimiziramo.
                    sez = self.igra.veljavne_poteze(nasprotnik(self.jaz))[0]
                    if sez == []:
                        sez = self.igra.veljavne_poteze(nasprotnik(self.jaz))[1]
                    najboljsa_poteza = None
                    vrednost_najboljse = Minimax.NESKONCNO
                    for (p1,p2) in sez:
                     
                        self.igra.naredi_potezo(p1,p2)
                        vrednost = self.minimax(globina-1, not maksimiziramo)[1]
                        self.igra.razveljavi()
                        if vrednost < vrednost_najboljse:
                            vrednost_najboljse = vrednost
                            najboljsa_poteza = (p1,p2)

                return (najboljsa_poteza, vrednost_najboljse)
            assert (najboljsa_poteza is not None), "Minimax: izračunana poteza je None"
            
        else:
            assert False, "Minimax: nedefinirano stanje igre "


#####################
## Razred Random:
#####################
            

class Random():
    # Ta razred uporablja računalnik in izbira naključne poteze
    def __init__(self,gui):
        self.gui = gui
        self.igra = None
        self.poteza = None
        self.prekinitev = False
        

    def najdi_potezo(self, igra):
        self.igra = igra
        self.prekinitev = False
        self.poteza = None
        # naključno izbere potezo
        (prejsna_pozicija, nova_pozicija) = self.nakljucna_izbira()
        self.igra = None
        if not self.prekinitev:
            logging.debug("Nakljucna izbira: ()".format(prejsna_pozicija, nova_pozicija))
            self.poteza = (prejsna_pozicija, nova_pozicija)
    def prekini(self):
        self.prekinitev = True


    def nakljucna_izbira(self):
        if self.prekinitev:
            logging.debug("Naključna izbira se prekinja")
            return (None, 0)
        zmagovalec = self.igra.stanje()
        if zmagovalec in (CRNI, BELI):
            # Igre je konec.
            return None
        elif zmagovalec == NI_KONEC:
            return(self.izberi())
        else:
            assert False, "Random: nedefinirano stanje igre"

    def izberi(self):
        (pojej, premakni) = self.gui.igra.veljavne_poteze(self.igra.na_potezi)
        if pojej == []:
            if len(premakni) > 0:
                return choice(premakni)
        elif len(pojej) > 0:
            return choice(pojej)
        


#############################
## Razred Alpha_beta:
#############################

class Alpha_beta():

    def __init__(self, globina):
        self.globina = globina
        self.prekinitev = False
        self.igra = None
        self.jaz = None
        self.poteza = None
        

    def prekini(self):
        self.prekinitev = True

    # Vrednost igre
    ZMAGA = 100000 #Vrednost zmage.
    NESKONCNO = ZMAGA + 100
    vrednost_dame = ZMAGA//10
    vrednost_st_figur = ZMAGA//100  
    vrednost_st_premikov = ZMAGA//1500
    vrednost_st_pojej = ZMAGA//1000

    
    
    def vrednost_polja(self):
        # Oceni vrednost polja, glede na število figur, ki jih še imamo,
        # glede na število možnih premikov in možnih odvzemov nasprotnikove
        # figure.
        st_figur = 0
        st_figur_naspr = 0
        dame = 0
        dame_naspr = 0
        for i in range(8):
            for j in range(8):
                if self.igra.deska[j][i] == Figura(self.igra.na_potezi):
                    st_figur += 1
                    if self.igra.deska[j][i].dama:
                        dame +=1
                elif self.igra.deska[j][i] == Figura(nasprotnik(self.igra.na_potezi)):
                    st_figur += 1
                    if self.igra.deska[j][i].dama:
                        dame_naspr += 1
                    
        (pojej1, premakni1) = self.igra.veljavne_poteze(self.igra.na_potezi)
        st_pojej1 = len(pojej1)
        st_premikov1 = len(premakni1)

        (pojej2, premakni2) = self.igra.veljavne_poteze(nasprotnik(self.igra.na_potezi))
        st_pojej2 = len(pojej2)
        st_premikov2 = len(premakni2)

        vrednost = (Minimax.vrednost_st_figur * st_figur + Minimax.vrednost_st_premikov * st_premikov1 + Minimax.vrednost_st_pojej * st_pojej1 + Minimax.vrednost_dame * dame - Minimax.vrednost_st_figur * st_figur_naspr - Minimax.vrednost_st_premikov * st_premikov2 - Minimax.vrednost_st_pojej * st_pojej2 - Minimax.vrednost_dame * dame_naspr)
        
        return vrednost



    def najdi_potezo(self,igra):
        # Najde najboljšo potezo v trenutnem stanju igre.
        self.igra = igra
        self.prekinitev = False
        self.jaz = self.igra.na_potezi
        self.poteza = None
        # Algoritem alpha-beta nam najde potezo.
        (poteza, vrednost) = self.alpha_beta(self.globina, True, -Alpha_beta.NESKONCNO, Alpha_beta.NESKONCNO)
        self.jaz = None
        self.igra = None
        if not self.prekinitev:
            logging.debug("Alpha-beta: poteza {0}, vrednost {1}".format(poteza, vrednost))
            self.poteza = poteza   


    def alpha_beta(self, globina, maksimiziramo, alpha, beta):
        # Glavna metoda alpha-beta
        if self.prekinitev:
            logging.debug("Alpha-beta prekinja, globina = {0}".format(globina))
            return (None, 0)
        zmagovalec = self.igra.stanje()
        if zmagovalec in (CRNI,BELI):
            # Če je igre konec, vrnemo njeno vrednost.
            if zmagovalec == self.jaz:
                return (None, Alpha_beta.ZMAGA)
            elif zmagovalec == nasprotnik(self.jaz):
                return (None, -Alpha_beta.ZMAGA)
            
        elif zmagovalec == NI_KONEC:
            self.preverjanje = True
            # Če igre še ni konec ločimo primera glede na globino.
            if globina == 0:
                return (None, self.vrednost_polja())
            else:
                
                if maksimiziramo:
                    # Maksimiziramo
                    a = alpha
                    b = beta
                    najboljsa_poteza = None
                    vrednost_najboljse = -Alpha_beta.NESKONCNO
                    
                    sez = self.igra.veljavne_poteze(self.jaz)[0]
                    if sez == []:
                        sez = self.igra.veljavne_poteze(self.jaz)[1]
                    
                    # Poiščemo potezo z najboljšo vrednostjo.
                    for (p1,p2) in sez:
                        self.igra.naredi_potezo(p1,p2)
                        vrednost = self.alpha_beta(globina-1, not maksimiziramo, alpha, beta)[1]
                        self.igra.razveljavi()
                        if vrednost > vrednost_najboljse:
                            vrednost_najboljse = vrednost
                            najboljsa_poteza = (p1,p2)
                        if vrednost > a:
                            a = vrednost
                        if b <= a:
                            break
                    
                    return (najboljsa_poteza, vrednost_najboljse)

                else:
                    # Minimiziramo
                    a = alpha
                    b = beta
                    najboljsa_poteza = None
                    vrednost_najboljse = Alpha_beta.NESKONCNO
                    sez = self.igra.veljavne_poteze(nasprotnik(self.jaz))[0]
                    if sez == []:
                        sez = self.igra.veljavne_poteze(nasprotnik(self.jaz))[1]
                    for (p1,p2) in sez:
                        self.igra.naredi_potezo(p1,p2)
                        vrednost = self.alpha_beta(globina-1, not maksimiziramo, alpha, beta)[1]
                        self.igra.razveljavi()
                        if vrednost < vrednost_najboljse:
                            vrednost_najboljse = vrednost
                            najboljsa_poteza = (p1,p2)
                        if vrednost < b:
                            b = vrednost
                        if b < a:
                            break
                    return (najboljsa_poteza, vrednost_najboljse)

                assert (najboljsa_poteza is not None), "Alpha-beta: izračunana poteza je None"
                
        else:
            assert False, "Alpha-beta: nedefinirano stanje igre "








            
                
                




    

