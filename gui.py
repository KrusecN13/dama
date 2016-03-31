###### Razred GUI: <h4>
##Vmesnik bo vseboval metode, s katerimi bo risal poteze na platno
#Celotni razred skupaj z metodami bo vsebovan v (glavni) datoteki dama.py.


from tkinter import *
from dama import *

#Definiramo razred, ki predstavlja naso aplikacijo
class Gui():

        TAG_FIGURA = 'figura'
        TAG_KROG = 'krog'
        
        def __init__(self, master=None):
                self.prenesene_poteze = [] 
                self.opravljen_klik1 = False 
                
                self.igra = None
                
                self.igrc = None
                self.igrb = None
                #init = stvari ki se zgodijo enkrat, vse kar se more zgodit, da
                #zaženemo grafični vmesnik
                master.configure(background = '#0000cd')

                #ustvarimo meni              
                menu = Menu(master)
                master.config(menu=menu)
                nova_igra_menu = Menu(menu)
                zapri_menu = Menu(menu)

                #nariši orodno vrstico v oknu
                menu.add_cascade(label = "Nova igra", menu = nova_igra_menu)
                menu.add_cascade(label = "Izhod", menu = zapri_menu)

                #s klikom na orodno vrstico izberemo moznosti
                

                #s klikom na orodno vrstico izberemo moznosti
                nova_igra_menu.add_command(label = "Clovek - Clovek",
                                           command = lambda: self.zacni_igro(Clovek(self),
                                                                             Clovek(self)))
                nova_igra_menu.add_command(label = "Clovek - Racunalnik",
                                           command = lambda: self.zacni_igro(Clovek(self),
                                                                             Racunalnik(self, Minimax(3))))
                nova_igra_menu.add_command(label = "Racunalnik - Clovek",
                                           command = lambda: self.zacni_igro(Racunalnik(self, Minimax(3)),
                                                                             Clovek(self)))
                nova_igra_menu.add_command(label = "Racunalnik - Racunalnik",
                                           command = lambda: self.zacni_igro(Racunalnik(self, Minimax(3)),
                                                                             Racunalnik(self, Minimax(3))))


                
                zapri_menu.add_command(label = "Izhod", command = lambda: self.izhod())

                self.kanvas = Canvas(master, width=800, height=800)
                self.kanvas.grid()

                self.napis = StringVar(master, value = "Dama")
                Label(master, textvariable = self.napis, background = '#87ceeb').grid(row=1, column=0)

                self.kanvas.bind("<Button-1>", self.kanvas_klika)
                
                self.ime_igralcaC = StringVar(master, value = 'Crni igralec')
                self.ime_igralcaB = StringVar(master, value = 'Beli igralec')
                kanvas_ime_igralcaC = Entry(master, width = 10, textvariable = self.ime_igralcaC, background = '#87ceeb')
                kanvas_ime_igralcaB = Entry(master, width = 10, textvariable = self.ime_igralcaB, background = '#87ceeb')
                kanvas_ime_igralcaC.grid()
                kanvas_ime_igralcaB.grid()

                # Nariši polja
                for x in range(0,800,100):
                        for y in range(0,800,100):
                                if ((x+y)//100)%2 == 0:
                                        self.kanvas.create_rectangle(x+(100),y+(100),
                                                    x,y,
                                                    outline="#000000", fill="#a0522d")

                                else:
                                       self.kanvas.create_rectangle(x+(100),y+(100),
                                                    x,y,
                                                    outline="#ffffff", fill="#deb887")
                                       
                self.zacni_igro(Clovek(self), Clovek(self))

        def postavi_figure(self):
                #self.slovar_figur = {} # XXX To bi moralo biti v self
                for i in range(8):
                        for j in range(3):
                                if (i+j)%2 == 0:
                                        a = self.kanvas.create_oval(i*100 + 15, j*100 + 15, i*100 + 85, j*100 + 85, fill='#000000', outline='#000000', tag = Gui.TAG_FIGURA) 
                                        #self.slovar_figur[Figura('CRNI',indeks = a)]=a
                                        fig = Figura(CRNI, indeks = a)
                                        self.igra.deska[j][i] = fig
                                        
                for i in range(8):
                        for j in range(5,8):
                                if (i+j)%2 == 0:
                                        a = self.kanvas.create_oval(i*100 + 15, j*100 + 15, i*100 + 85, j*100 + 85, fill='#ffffff', outline='#000000', tag = Gui.TAG_FIGURA) 
                                        fig = Figura(BELI, indeks = a)
                                        #self.slovar_figur[fig]=a
                                        self.igra.deska[j][i] = fig

                                        
                #print(self.igra.deska)


                
        def zacni_igro(self, igrc, igrb):
                # najprej ustavimo vsa vlakna, ki še razmišljajo ter pobrišemo polje
                self.igra = Igra()
                self.prekini_igralca()
                self.kanvas.delete(Gui.TAG_FIGURA)
                self.kanvas.delete(Gui.TAG_KROG)
                self.postavi_figure()                

        
                
                self.igrc = igrc
                self.igrb = igrb

                self.napis.set("Na potezi je CRNI")
                self.igrc.igraj()

            

        def koncaj_igro(self,zmagovalec):
                if zmagovalec == CRNI:
                        self.napis.set("Zmagal je CRNI!")
                elif zmagovalec == BELI:
                        self.napis.set("Zmagal je BELI!")

        def izhod(self):
                # zapri okno, prekini igralce,                 
                self.prekini_igralca()
                master.destroy()
                
        def prekini_igralca(self):
                logging.debug("Prekinjam igralce")
                if self.igra.na_potezi == CRNI and self.igrc:
                        self.igrc.prekini()
                elif self.igrb:
                        self.igrb.prekini()
                
        def zbrisi_figuro(self,polje):
                (a,b) = polje
                self.kanvas.delete(self.igra.deska[a][b].indeks)
                self.igra.deska[a][b] = None
                
        

        
        def kanvas_klika(self, event):
                if not self.opravljen_klik1:
                        #print('zacetek faze 1')
                        # To je prvi klik
                        i = event.x // 100
                        j = event.y // 100
                        #print('na potezi   =',self.igra.na_potezi)
                        (pojej,premakni) = self.igra.veljavne_poteze(self.igra.na_potezi)
                        print("POJEJ",pojej)
                        pojej_iz_polja = []
                        premakni_iz_polja = []

                        # # Alternativna možna logika
                        # if len(pojej) > 0 or len(premakni) > 0:
                        #         # Možna je poteza
                        #         if len(pojej) > 0:
                        #                 # moramo pojesti
                        #                 pass
                        #         else:
                        #                 # Premikamo se
                        #                 pass
                        #         # Kar je skupno obema potezama
                        #         if self.prvi_klik: # gremo v drugo fazo klika
                        #                 # oznacimo zeton s create_rectangle, oglejta si tag="..." v
                        #                 # create_rectangle.
                        # else:
                        #         # Ni možne poteze, kaj sploh delamo tu?

                        if pojej == [] and premakni == []:
                                #print('oba seznama sta prazna')
                                self.koncaj_igro(nasprotnik(self.igra.na_potezi)) 
                                return # XXX tricky, morda je bolje narediti if-else tako, da se takoj vidi, da se koda spodaj ne izvaja
                        
                        else:
                                if premakni != []:
                                        for ((x,y), (a,b)) in premakni:
                                                if x == i and y == j:
                                                        premakni_iz_polja.append(((i,j),(a,b)))
                                if pojej != []:
                                         for ((x,y), (a,b)) in pojej:
                                                if x == i and y == j:
                                                        pojej_iz_polja.append(((i,j),(a,b)))
                        #print(pojej_iz_polja)
               
                        if pojej != [] and pojej_iz_polja == []:
                                self.napis.set("Izberi figuro, ki mora pojesti!")
                                return
                        if len(pojej_iz_polja) > 0 or len(premakni_iz_polja) > 0:
                                #Možna je poteza
                                if len(pojej_iz_polja) > 0:
                                        
                                        sez_vseh_iz_pozicije = pojej_iz_polja
                                        for ((i,j),(a,b)) in sez_vseh_iz_pozicije:
                                                 self.kanvas.create_oval(a*100 + 30, b*100 + 30,
                                                                             a*100 + 70, b*100 + 70,
                                                                             outline="#000000", fill="#00bfff", tag = Gui.TAG_KROG)
                                elif len(premakni_iz_polja) > 0:
                                        sez_vseh_iz_pozicije = premakni_iz_polja
                                        for ((i,j),(a,b)) in sez_vseh_iz_pozicije:
                                                self.kanvas.create_oval(a*100 + 30, b*100 + 30,
                                                                             a*100 + 70, b*100 + 70,
                                                                             outline="#000000", fill="#00bfff", tag = Gui.TAG_KROG)
                        else:
                                self.napis.set("Izberi figuro, ki lahko naredi potezo!")
                                return

                                
                                
                        #print((i,j))
                        #print(sez_vseh_iz_pozicije)
                        if len(sez_vseh_iz_pozicije) > 0:
                                # Gremo v drugo fazo klika
                                # XXX kaj pa, če bi označili še tistega, na katerega je kliknil?
                                #print ("Gremo v fazo 2")
                                self.prenesene_poteze = sez_vseh_iz_pozicije
                                self.opravljen_klik1 = True

                else:
                        #print ("Pa smo v fazi 2")
                        # XXX takole pobrišemo: self.kanvas.delete("oznaka")
                        sez_vseh_iz_pozicije = self.prenesene_poteze
                        #print(sez_vseh_iz_pozicije)
                        assert (len(sez_vseh_iz_pozicije) > 0), "druga faza klika"
                        # To je drugi klik
                        i = event.x // 100
                        j = event.y // 100
                        for (a,b),(c,d) in sez_vseh_iz_pozicije:
                                 if (c,d) == (i,j):
                                        # Lahko izvedemo potezo
                                        #print("naredimo potezo {0}".format(((a,b),(c,d))))
                                        if self.igra.na_potezi == CRNI:
                                                 self.igrc.klik(((a,b),(c,d)))
                                        elif self.igra.na_potezi == BELI:
                                                self.igrb.klik(((a,b),(c,d)))
                                        else:
                                                assert False, "čuden igralec"
                        print("smo končali fazo 2")
                        # Gremo nazaj v fazo 1
                        self.prenesene_poteze = []
                        self.opravljen_klik1 = False
                        self.kanvas.delete(Gui.TAG_KROG)

        def naredi_potezo(self,a,p):
                # a so stare koordinate, ki jih dobimo s klikom, p pa nove

                (k,l) = a
                (m,n) = p
                print('premik',a,p)
                #print(self.igra.deska)
                id_1 = self.igra.deska[l][k].indeks
                print("indeks",id_1)
                igralec = self.igra.na_potezi
                (pojej,premakni) = self.igra.veljavne_poteze(self.igra.na_potezi)
                r = self.igra.naredi_potezo(a,p)
                #print("za r-jom")
                if (a,p) in pojej:
                        print("pred coords", a)
                        self.kanvas.coords(id_1,100*m +15,100*n + 15,100*m + 85,100*n+85)
                        self.zbrisi_figuro(100*((m+k)//2),100*((l+n)//2))
                elif (a,p) in premakni:
                        print("pred coords")
                        self.kanvas.coords(id_1,100*m +15,100*n + 15,100*m + 85,100*n+85)
                        print("za coords")
                        print(self.igra.deska)
                        
                
                self.napis.set("Na potezi je {0}".format(self.igra.na_potezi))
                
                                                    
                        
                        
                
                
                

                
                
                        
                        
                        
        

        
            
            


 #GLAVNI PROGRAM
root = Tk()
root.title("Dama")
aplikacija = Gui(root)
root.mainloop()

