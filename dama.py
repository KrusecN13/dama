##
###### Razred Igra: <h4>
##Metode znotraj razreda Igra bodo:
##* naredi_potezo(self,i,j), ki se bo razdelila na podmetodi premakni(self,i,j) in pojej(self,i,j)
##* razveljavi(self)
##* na_potezi(self)
##* je_veljavna(self,i,j)
##* zmagovalec(self)



class Figura():
    def __init__(self, x, y, barva, dama = False):
        self.x = x
        self.y = y
        self.barva = barva
        self.dama = dama
        
        
igralec_C = "C"
igralec_B = "B"

def nasprotnik(igralec):
    if igralec == igralec_C:
        return igralec_B
    elif igralec == igralec_B:
        return igralec_C
    else:
        assert False
    
    

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
        
        
        self.na_potezi = igralec_C
        self.zgodovina = [(self.deska, igralec_C)]

        # seznam vseh belih in crnih figur
        bele = []
        for i in range(8):
            for j in range(8):
                if self.deska[i][j] == 'B':
                    f = Figura(i,j,bela)
                    bele.append(f)

        crne = []
        for i in range(8):
            for j in range(8):
                if self.deska[i][j] == 'C':
                    f = Figura(i,j,crna)
                    crne.append(f)
        
        
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
        copy = Igra()
        copy.deska = [self.deska[j][:] for j in range(8)]
        copy.na_potezi = self.na_potezi
        return copy

    def je_veljavna(self, i, j):
        for i in range(8):
            for j in range(8):
                if self.zgodovina[-1][i][j] == None:
                    return True
        return False

    
##    def stanje(self):
##        # ugotovi, ali že imamo zmagovalca in ga vrne, oz.
##        # poklièe funkcijo naredi_potezo
##        for i in self.deska:
##            for j in i:
##                if not naredi_potezi(nasprotnik(self.na_potezi)):
##                    return 
##                        
##        
        
###?? kako bi ustvarila seznam vseh belih/crnih figur?
## (da bi lahko klicala funkcijo na seznamu vseh figur ene barve)
    def pojej(self, prva, druga):

# seznama bele in črne ustrezno spremeni
        iks = prva.x
        ipsilon = prva.y
        zeta = druga.x
        teta = druga.y
        if prva.dama:
            if prva.barva != druga.barva:
                if prva.x - druga.x == 1 and (prva.y + 1) == druga.y and prva.deska[self.x -2 ][prva.y +2] == None:
                    prva.x = iks - 2
                    prva.y = ipsilon + 2
                    
                    zbrisi(iks, ipsilon)
                    zbrisi(zeta, teta)

                    
                elif prva.x - druga.x == -1 and (prva.y + 1) == druga.y and prva.deska[self.x + 2][prva.y +2] == None:
                    prva.x = iks + 2
                    prva.y = ipsilon + 2
                    
                    zbrisi(iks, ipsilon)
                    zbrisi(zeta, teta)
                elif prva.x - druga.x == 1 and (prva.y - 1) == druga.y and prva.deska[prva.x -2 ][prva.y -2] == None:
                    prva.x = iks - 2
                    prva.y = ipsilon - 2
                    
                    zbrisi(iks, ipsilon)
                    zbrisi(zeta, teta)

                elif prva.x - druga.x == -1 and (prva.y - 1) == druga.y and prva.deska[prva.x + 2][prva.y -2] == None:
                    prva.x = iks + 2
                    prva.y = ipsilon - 2
                    
                    zbrisi(iks, ipsilon)
                    zbrisi(zeta, teta)
                if prva.barva == crna:
                    self.deska[prva.x][prva.y] = igralec_C
                elif prva.barva == bela:
                    self.deska[prva.x][prva.y] = igralec_B
                if prva.bela:
                    bele.remove(Figura(iks,ipsilon,bela))
                    crne.remove(Figura(zeta,teta,crna))
                    bele.append(Figura(prva.x,prva.y,bela))
                elif prva.crna:
                    crne.remove(Figura(iks,ipsilon,bela))
                    bele.remove(Figura(zeta,teta,crna))
                    crne.append(Figura(prva.x,prva.y,bela))
                


        
        elif prva.barva == crna:
            if druga.barva == bela:
                if prva.x - druga.x == 1 and (prva.y + 1) == druga.y and prva.deska[prva.x -2 ][prva.y +2] == None:
                    prva.x = iks - 2
                    prva.y = ipsilon + 2
                    
                    zbrisi(iks, ipsilon)
                    zbrisi(zeta, teta)
                elif prva.x - druga.x == -1 and (prva.y + 1) == druga.y and prva.deska[prva.x + 2][prva.y +2] == None:
                    prva.x = iks + 2
                    prva.y = ipsilon + 2
                    
                    zbrisi(iks, ipsilon)
                    zbrisi(zeta, teta)
                self.deska[prva.x][prva.y] = igralec_C
                crne.remove(Figura(iks,ipsilon,bela))
                bele.remove(Figura(zeta,teta,crna))
                crne.append(Figura(prva.x,prva.y,bela))
        elif prva.barva == bela:
            if druga.barva == crna:
                if prva.x - druga.x == 1 and (prva.y - 1) == druga.y and prva.deska[prva.x -2 ][prva.y -2] == None:
                    prva.x = iks - 2
                    prva.y = ipsilon - 2
                    
                    zbrisi(iks, ipsilon)
                    zbrisi(zeta, teta)
                elif prva.x - druga.x == -1 and (prva.y - 1) == druga.y and prva.deska[prva.x + 2][prva.y -2] == None:
                    prva.x = iks + 2
                    prva.y = ipsilon - 2
                    
                    zbrisi(iks, ipsilon)
                    zbrisi(zeta, teta)
                self.deska[prva.x][prva.y] = igralec_B
                bele.remove(Figura(iks,ipsilon,bela))
                crne.remove(Figura(zeta,teta,crna))
                bele.append(Figura(prva.x,prva.y,bela))
        
        else:
            assert False, "Figura ne more pojesti"
                
            

            
    def zbrisi(self,i,j):
        self.deska[i][j] = None
        
        
    def premakni(self, figura, i, j):

        iks = figura.x
        ipsilon = figura.y

        if figura.dama:
            if abs(figura.x - i)==1 and abs(figura.y - j) == 1 and 0<=i<=7 and 0<=j<=7:
                figura.x = i
                figura.y = j
                zbrisi(iks, ipsilon)
                if figura.barva == crna:
                    self.deska[i][j] = igralec_C
                elif figura.barva == bela:
                    self.deska[i][j] = igralec_B
                
                
        elif figura.barva == crna:
            if abs(figura.x - i)==1 and (figura.y + 1) == j and 0<=i<=7 and 0<=j<=7:
                figura.x = i
                figura.y = j
                zbrisi(iks, ipsilon)
                self.deska[i][j] = igralec_C

        elif figura.barva == bela:
            if abs(figura.x - i)==1 and (figura.y - 1) == j and 0<=i<=7 and 0<=j<=7:
                figura.x = i
                figura.y = j
                zbrisi(iks, ipsilon)
                self.deska[i][j] = igralec_B
# seznama bele in črne ustrezno spremeni                
        if figura.bela:
            bele.remove(Figura(iks,ipsilon,bela))
            bele.append(Figura(figura.x,figura.y,bela))
        if figura.crna:
            crne.remove(Figura(iks,ipsilon,bela))
            crne.append(Figura(figura.x,figura.y,bela))
                

                   
    
    def naredi_potezo(self, druga):
    # če je poteza neveljavna ne naredi ničesar
    # če je poteza veljavna jo izvede
        if not je_veljavna(self, i, j):
            return None
        
        
        
    







        
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


    







    

