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

    
    def zmagovalec(self):
        pass
    
    def pojej(self, druga):
        iks = self.x
        ipsilon = self.y
        zeta = druga.x
        teta = druga.y
##        if self.dama:
##            
##            if abs(self.x - i)==1 and abs(self.y - j) == 1 and 0<=i<=7 and 0<=j<=7
##            and :
##                self.x = i
##                self.y = j
##                zbrisi(iks, ipsilon)
        if self.barva == crna:
            if druga.barva == bela:
                if self.x - druga.x == 1 and (self.y + 1) == druga.y and self.deska[self.x -2 ][self.y +2] == None:
                    self.x = iks - 2
                    self.y = ipsilon + 2
                    
                    zbrisi(iks, ipsilon)
                    zbrisi(zeta, teta)
                if self.x - druga.x == -1 and (self.y + 1) == druga.y and self.deska[self.x + 2][self.y +2] == None:
                    self.x = iks + 2
                    self.y = ipsilon + 2
                    
                    zbrisi(iks, ipsilon)
                    zbrisi(zeta, teta)
        if self.barva == bela:
            if druga.barva == crna:
                if self.x - druga.x == 1 and (self.y - 1) == druga.y and self.deska[self.x -2 ][self.y -2] == None:
                    self.x = iks - 2
                    self.y = ipsilon - 2
                    
                    zbrisi(iks, ipsilon)
                    zbrisi(zeta, teta)
                if self.x - druga.x == -1 and (self.y - 1) == druga.y and self.deska[self.x + 2][self.y -2] == None:
                    self.x = iks + 2
                    self.y = ipsilon - 2
                    
                    zbrisi(iks, ipsilon)
                    zbrisi(zeta, teta)
                
            

            
    def zbrisi(self,i,j):
        self.deska[i][j] = None
        
    def premakni(self, i, j):
        iks = self.x
        ipsilon = self.y
        if not je_veljavna(self, i, j):
            return None
        
        if self.dama:
            if abs(self.x - i)==1 and abs(self.y - j) == 1 and 0<=i<=7 and 0<=j<=7:
                self.x = i
                self.y = j
                zbrisi(iks, ipsilon)    
                
                
        elif self.barva == crna:
            if abs(self.x - i)==1 and (self.y + 1) == j and 0<=i<=7 and 0<=j<=7:
                self.x = i
                self.y = j
                zbrisi(iks, ipsilon)

        elif self.barva == bela:
            if abs(self.x - i)==1 and (self.y - 1) == j and 0<=i<=7 and 0<=j<=7:
                self.x = i
                self.y = j
                zbrisi(iks, ipsilon)            
                

                   
    
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


    







    

