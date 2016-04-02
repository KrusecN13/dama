from tkinter import *
from dama import *

#################################################################
## Razred Gui (uporabniški vmesnik) predstavlja našo aplikacijo:
#################################################################

class Gui():
        # Oznake za grafične elemente v self.kanvas

        # Oznaka za vse figure.
        TAG_FIGURA = 'figura'

        # Oznaka za označitev možnih potez iz mesta.
        TAG_KROG = 'krog'
        
        def __init__(self, master=None):
                self.prenesene_poteze = [] # Veljavne poteze za po prvem kliku
                self.opravljen_klik1 = False # Prvi klik je opravljen.
                
                self.igra = None # Objekt, ki predstavlja igro.
                
                self.igrc = None # Objekt, ki igra s crnimi figurami
                self.igrb = None # Objekt, ki igra z belimi figurami

                # Ozadje
                master.configure(background = '#0000cd')

                # Ustvarimo meni.              
                menu = Menu(master)
                master.config(menu=menu)
                nova_igra_menu = Menu(menu)
                zapri_menu = Menu(menu)

                # Nariši orodno vrstico v oknu.
                menu.add_cascade(label = "Nova igra", menu = nova_igra_menu)
                menu.add_cascade(label = "Izhod", menu = zapri_menu)

                
                #S klikom na orodno vrstico izberemo moznosti igralcev.
                nova_igra_menu.add_command(label = "Clovek - Clovek",
                                           command = lambda: self.zacni_igro(Clovek(self),
                                                                             Clovek(self)))
                nova_igra_menu.add_command(label = "Clovek - Racunalnik (lažje)",
                                           command = lambda: self.zacni_igro(Clovek(self),
                                                                             Racunalnik(self, Random(self))))
                nova_igra_menu.add_command(label = "Clovek - Racunalnik (težje)",
                                           command = lambda: self.zacni_igro(Clovek(self),
                                                                             Racunalnik(self, Minimax(3))))

                
                nova_igra_menu.add_command(label = "Racunalnik - Clovek (lažje)",
                                           command = lambda: self.zacni_igro(Racunalnik(self, Random(self)),
                                                                             Clovek(self)))
                nova_igra_menu.add_command(label = "Racunalnik - Clovek (težje)",
                                           command = lambda: self.zacni_igro(Racunalnik(self, Minimax(3)),
                                                                             Clovek(self)))
                
                nova_igra_menu.add_command(label = "Racunalnik(Minimax) - Racunalnik(Minimax)",
                                           command = lambda: self.zacni_igro(Racunalnik(self, Minimax(3)),
                                                                             Racunalnik(self, Minimax(3))))

                nova_igra_menu.add_command(label = "Racunalnik(Minimax) - Racunalnik(Random)",
                                           command = lambda: self.zacni_igro(Racunalnik(self, Minimax(3)),
                                                                             Racunalnik(self, Random(self))))
                nova_igra_menu.add_command(label = "Racunalnik(Random) - Racunalnik(Minimax)",
                                           command = lambda: self.zacni_igro(Racunalnik(self, Random(self)),
                                                                             Racunalnik(self, Minimax(3))))

                # Zapri aplikacijo.
                zapri_menu.add_command(label = "Izhod", command = lambda: self.izhod())

                # Igralno polje.
                self.kanvas = Canvas(master, width=800, height=800)
                self.kanvas.grid()

                # Napis, ki prikazuje stanje igre.
                self.napis = StringVar(master, value = "Dama")
                Label(master, textvariable = self.napis, background = '#87ceeb').grid(row=1, column=0)

                # Naročimo se na dogodek Button-1 na self.kanvas,
                # da bo zaznal klike.
                self.kanvas.bind("<Button-1>", self.kanvas_klika)

                # Uporabniki lahko napišejo svoje ime.
                self.ime_igralcaC = StringVar(master, value = 'Crni igralec')
                self.ime_igralcaB = StringVar(master, value = 'Beli igralec')
                kanvas_ime_igralcaC = Entry(master, width = 10, textvariable = self.ime_igralcaC, background = '#87ceeb')
                kanvas_ime_igralcaB = Entry(master, width = 10, textvariable = self.ime_igralcaB, background = '#87ceeb')
                kanvas_ime_igralcaC.grid()
                kanvas_ime_igralcaB.grid()

                # Nariši vsa polja.
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

                # Prični igro v načinu človek - človek.                       
                self.zacni_igro(Clovek(self), Clovek(self))

        def postavi_figure(self):
                # Metoda, ki postavi figure na self.kanvas in na desko (v igri)
                # in vsaki figuri nastavi svoj indeks.
                for i in range(8):
                        for j in range(3):
                                if (i+j)%2 == 0:
                                        a = self.kanvas.create_oval(i*100 + 15, j*100 + 15,
                                                                    i*100 + 85, j*100 + 85,
                                                                    fill='#000000', outline='#000000',
                                                                    tag = Gui.TAG_FIGURA) 
                                        fig = Figura(CRNI, indeks = a)
                                        self.igra.deska[j][i] = fig
                                        
                for i in range(8):
                        for j in range(5,8):
                                if (i+j)%2 == 0:
                                        a = self.kanvas.create_oval(i*100 + 15, j*100 + 15,
                                                                    i*100 + 85, j*100 + 85,
                                                                    fill='#ffffff', outline='#000000',
                                                                    tag = Gui.TAG_FIGURA) 
                                        fig = Figura(BELI, indeks = a)
                                        self.igra.deska[j][i] = fig

                                        
                
                
        def zacni_igro(self, igrc, igrb):
                # Nastavi stanje igre na začetek in za igralca uporabi igrc in igrb.
                
                # Najprej ustavimo vsa vlakna, ki še razmišljajo ter pobrišemo vse objekte.
                self.prekini_igralca()
                self.kanvas.delete(Gui.TAG_FIGURA)
                self.kanvas.delete(Gui.TAG_KROG)
                # Ustvarimo novo igro ter postavimo figure.
                self.igra = Igra()
                self.postavi_figure()                

                # Shranimo igralce v igri.
                self.igrc = igrc
                self.igrb = igrb

                # Na začetku vedno začne igralec s črnimi figurami.
                self.napis.set("Na potezi je CRNI")
                self.igrc.igraj()

            

        def koncaj_igro(self,zmagovalec):
                # Nastavi stanje igre na konec in izpiše zmagovalca.
                if zmagovalec == CRNI:
                        self.napis.set("Zmagal je CRNI!")
                elif zmagovalec == BELI:
                        self.napis.set("Zmagal je BELI!")

        def izhod(self):
                # Zapre okno in prekine igralce.                 
                self.prekini_igralca()
                master.destroy()
                
        def prekini_igralca(self):
                # Igralce obvesti, da naj nehajo razmišljati.
                logging.debug("Prekinjam igralce")
                if self.igrc:
                        self.igrc.prekini()
                if self.igrb:
                        self.igrb.prekini()
                
        def zbrisi_figuro(self,polje):
                # Metoda, ki zbriše figuro iz self.kanvas in iz self.igra.deska
                (a,b) = polje
                self.kanvas.delete(self.igra.deska[b][a].indeks)
                self.igra.deska[b][a] = None
                
        
        
        def kanvas_klika(self, event):
                # Možna sta dva klika. Da preverimo, če je bil klik že opravljen
                # si pomagamo s spremenljivko self.opravljen_klik1.
                if not self.opravljen_klik1:
                        # Če nismo še kliknili na kanvas.
                        i = event.x // 100
                        j = event.y // 100
                        (pojej,premakni) = self.igra.veljavne_poteze(self.igra.na_potezi)
                        # Ustvarimo seznama možnih potez iz določenega polja.
                        pojej_iz_polja = []
                        premakni_iz_polja = []

                        if pojej == [] and premakni == []:
                                # Če ni več možnih potez končamo igro in klik ignoriramo.
                                self.koncaj_igro(nasprotnik(self.igra.na_potezi)) 
                                return 
                        
                        else:
                                # Imamo še možnih potez, ki jih zapišemo v seznama pojej_iz_polja in
                                # premakni_iz_polja.
                                if premakni != []:
                                        for ((x,y), (a,b)) in premakni:
                                                if x == i and y == j:
                                                        premakni_iz_polja.append(((i,j),(a,b)))
                                if pojej != []:
                                         for ((x,y), (a,b)) in pojej:
                                                if x == i and y == j:
                                                        pojej_iz_polja.append(((i,j),(a,b)))

                        # Premakniti moramo figuro, ki lahko poje nasprotnikovo.               
                        if pojej != [] and pojej_iz_polja == []:
                                self.napis.set("Izberi figuro, ki mora pojesti!")
                                return
                        
                        if len(pojej_iz_polja) > 0 or len(premakni_iz_polja) > 0:
                                # Vse možne poteze označimo na kanvasu, da uporabnik lahko izbere,
                                # katero bo naredil.
                                if len(pojej_iz_polja) > 0:
                                        
                                        sez_vseh_iz_pozicije = pojej_iz_polja
                                        for ((i,j),(a,b)) in sez_vseh_iz_pozicije:
                                                 self.kanvas.create_rectangle(a*100 + 30, b*100 + 30,
                                                                             a*100 + 70, b*100 + 70,
                                                                             outline="#000000",
                                                                              fill="#660033",
                                                                              tag = Gui.TAG_KROG)
                                elif len(premakni_iz_polja) > 0:
                                        sez_vseh_iz_pozicije = premakni_iz_polja
                                        for ((i,j),(a,b)) in sez_vseh_iz_pozicije:
                                                self.kanvas.create_rectangle(a*100 + 30, b*100 + 30,
                                                                             a*100 + 70, b*100 + 70,
                                                                             outline="#000000",
                                                                             fill="#660033",
                                                                             tag = Gui.TAG_KROG)
                        else:
                                # Figura, ki jo je izbral uporabnik se ne more premakniti, a se
                                # lahko premakne katera druga.
                                self.napis.set("Izberi figuro, ki lahko naredi potezo!")
                                return

                                
                                
                        if len(sez_vseh_iz_pozicije) > 0:
                                # Gremo v drugo fazo klika in si zapomnimo vse možne poteze iz polja.
                                
                                self.prenesene_poteze = sez_vseh_iz_pozicije
                                self.opravljen_klik1 = True

                else:
                        
                        sez_vseh_iz_pozicije = self.prenesene_poteze
                        # Imamo možne poteze.
                        assert (len(sez_vseh_iz_pozicije) > 0), "druga faza klika"
                        
                        # To je drugi klik.
                        i = event.x // 100
                        j = event.y // 100
                        for (a,b),(c,d) in sez_vseh_iz_pozicije:
                                 if (c,d) == (i,j):
                                        # Lahko izvedemo potezo s pomočjo metode klik, ki kliče metodo
                                        # naredi_potezo za človeka oz. za računalnik klike ignorira.
                                        if self.igra.na_potezi == CRNI:
                                                 self.igrc.klik(((a,b),(c,d)))
                                        elif self.igra.na_potezi == BELI:
                                                self.igrb.klik(((a,b),(c,d)))
                                        else:
                                                assert False, "čuden igralec"
                        
                        # Gremo nazaj v fazo 1 - pred opravljenim prvim klikom.
                        self.prenesene_poteze = []
                        self.opravljen_klik1 = False
                        self.kanvas.delete(Gui.TAG_KROG)

        def naredi_potezo(self,a,p):
                # a so stare koordinate, ki jih dobimo s klikom, p pa nove.

                # Najprej povlečemo potezo v igri, nato na kanvasu.

                (k,l) = a
                (m,n) = p
                id_1 = self.igra.deska[l][k].indeks
                igralec = self.igra.na_potezi
                (pojej,premakni) = self.igra.veljavne_poteze(self.igra.na_potezi)
                r = self.igra.naredi_potezo(a,p)
                if igralec == CRNI:
                        self.napis.set("Na potezi je BELI")
                elif igralec == BELI:
                        self.napis.set("Na potezi je CRNI")
                if (a,p) in pojej:
                        # Figuro premaknemo, nasprotnikovo pa zbrišemo.
                        self.kanvas.coords(id_1,100*m +15,100*n + 15,100*m + 85,100*n+85)
                        self.zbrisi_figuro(((m+k)//2,(l+n)//2))
                elif (a,p) in premakni:
                        # Figuro premaknemo.
                        self.kanvas.coords(id_1,100*m +15,100*n + 15,100*m + 85,100*n+85)
                        
                if self.igra.deska[n][m].dama:
                        # Če je figura postala dama jo drugače obarvamo.
                        if self.igra.deska[n][m].igralec == BELI:
                                self.kanvas.itemconfig(id_1, fill = "#66B2FF")
                        elif self.igra.deska[n][m].igralec == CRNI:
                                self.kanvas.itemconfig(id_1, fill = "#660000")
                print(self.igra.stanje())
                if self.igra.stanje() != "ni konec":
                        self.koncaj_igro(nasprotnik(self.igra.na_potezi))
                #določi, ali mora računalnik kaj narediti glede na to, ali je na potezi
                if self.igrc != Clovek(self) and self.igrb != Clovek(self):
                        if self.igra.na_potezi == BELI:
                                self.igrb.igraj()
                        elif self.igra.na_potezi == CRNI:
                                self.igrc.igraj()
                elif self.igrc != Clovek(self):
                        if self.igra.na_potezi == CRNI:
                                self.igrc.igraj()
                elif self.igrb != Clovek(self):
                        if self.igra.na_potezi == BELI:
                                self.igrb.igraj()
                        
                

                
                
                                                    
                        
                        
                
                
                

                
                
                        
                        
                        
        

        
            
            


 #GLAVNI PROGRAM
root = Tk()
root.title("Dama")
aplikacija = Gui(root)
root.mainloop()

