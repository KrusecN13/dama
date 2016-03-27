###### Razred GUI: <h4>
##Vmesnik bo vseboval metode, s katerimi bo risal poteze na platno
#Celotni razred skupaj z metodami bo vsebovan v (glavni) datoteki dama.py.


from tkinter import *
from dama import *

#Definiramo razred, ki predstavlja naso aplikacijo
class Gui():

        TAG_FIGURA = 'figura'
        
        def __init__(self, master=None):
                self.igra = None
                
                self.igrc = None
                self.igrb = None
            #init = stvari ki se zgodijo enkrat, vse kar se more zgodit, da
            #zaženemo grafični vmesnik
                master.configure(background = 'orange')

        #ustvarimo meni              
                menu = Menu(master)
                master.config(menu=menu)
                nova_igra_menu = Menu(menu)
                zapri_menu = Menu(menu)
        #nariši orodno vrstico v oknu
                menu.add_cascade(label = "Nova igra", menu = nova_igra_menu)
                menu.add_cascade(label = "Izhod", menu = zapri_menu)
        #s klikom na orodno vrstico izberemo moznosti
                nova_igra_menu.add_command(label = "Clovek - Clovek",
                                           command = lambda: self.zacni_igro(Clovek(self, self.ime_igralcaC),
                                                                             Clovek(self, self.ime_igralcaB)))
                nova_igra_menu.add_command(label = "Clovek - Racunalnik",
                                           command = lambda: self.zacni_igro(Clovek(self, self.ime_igralcaC),
                                                                             Racunalnik(self, Minimax(globina))))
                nova_igra_menu.add_command(label = "Racunalnik - Clovek",
                                           command = lambda: self.zacni_igro(Racunalnik(self, Minimax(globina)),
                                                                             Clovek(self, self.ime_igralcaB)))
                nova_igra_menu.add_command(label = "Racunalnik - Racunalnik",
                                           command = lambda: self.zacni_igro(Racunalnik(self, Minimax(globina)),
                                                                             Racunalnik(self, Minimax(globina))))
                zapri_menu.add_command(label = "Izhod", command = lambda: self.izhod())

                self.kanvas = Canvas(master, width=800, height=800)
                self.kanvas.grid()

                self.napis = StringVar(master, value = "Dama")
                Label(master, textvariable = self.napis, background = 'orange').grid(row=1, column=0)

                self.igra = Igra()
                self.kanvas.bind("<Button-1>", self.kanvas_klik1)
                
                self.ime_igralcaC = StringVar(master, value = 'Crni igralec')
                self.ime_igralcaB = StringVar(master, value = 'Beli igralec')
                kanvas_ime_igralcaC = Entry(master, width = 10, textvariable = self.ime_igralcaC, background = 'orange')
                kanvas_ime_igralcaB = Entry(master, width = 10, textvariable = self.ime_igralcaB, background = 'orange')
                kanvas_ime_igralcaC.grid()
                kanvas_ime_igralcaB.grid()

                
                self.postavi_figure()
                slovar_figur = {}
                for i in range(8):
                        for j in range(3):
                                if (i+j)%2 == 0:
                                        a = self.kanvas.create_oval(i*100 + 15, j*100 + 15, i*100 + 85, j*100 + 85, fill='#7D26D9', outline='#000000') 
                                        slovar_figur[Figura('igrC')]=a
                for i in range(8):
                        for j in range(5,8):
                                if (i+j)%2 == 0:
                                        a = self.kanvas.create_oval(i*100 + 15, j*100 + 15, i*100 + 85, j*100 + 85, fill='#9EB5BA', outline='#000000') 
                                        slovar_figur[Figura('igrB')]=a
                                        
                #print(slovar_figur)
##          na koncu inita: izbira igralcev (veže na funkcijo izbira_igralca,
##          ta dela naprej)
#coords

        def postavi_figure(self):
                for x in range(0,800,100):
                        for y in range(0,800,100):
                                if ((x+y)//100)%2 == 0:
                                        self.kanvas.create_rectangle(x+(100),y+(100),
                                                    x,y,
                                                    outline="#000000", fill="#000000")

                                else:
                                       self.kanvas.create_rectangle(x+(100),y+(100),
                                                    x,y,
                                                    outline="#ffffff", fill="#CD8527")


                
        def zacni_igro(self, igrc, igrb):
        # najprej ustavimo vsa vlakna, ki še razmišljajo ter pobrišemo polje
                self.prekini_igralca()
                self.kanvas.delete(Gui.TAG_FIGURA)
                self.postavi_figure()
                

                self.igra = Igra()
                
                self.igrc = igrc
                self.igrb = igrb

                self.napis.set("Na potezi je crni")
                self.igrc.igraj()
                
                
            

        def koncaj_igro(self,zmagovalec):
                if zmagovalec == igrC:
                        self.napis.set("Zmagal je crni!")
                elif zmagovalec == igrB:
                        self.napis.set("Zmagal je beli!")

        def izhod(self):
# zapreti okno, prekiniti igralce, 
                
                self.prekini_igralca()
                master.destroy()
                
        def prekini_igralca(self):
                logging.debug("Prekinjam igralce")
                self.igra.na_potezi.prekini()


        def kanvas_klik1(self,event1):
        # dobiva koordinate stare pozicije
                i = event1.x // 100
                j = event1.y // 100
                sez_vseh_iz_pozicije = []
                (pojej,premakni) = self.igra.veljavne_poteze(self.igra.na_potezi)
                if pojej == [] and premakni == []:
                        pass
                elif pojej == []:
                        for a in range(8):
                                for b in range(8):
                                        if ((i,j),(a,b)) in premakni:
                                                sez_vseh_iz_pozicije.append(((i,j),(a,b)))
                                                self.kanvas.create_rectangle(i*100 - 50,i*100 + 50,
                                                    i*100 - 50,i*100 + 50,
                                                    outline="#000000", fill="#1020FF")         
                        
                else:
                        for a in range(8):
                                for b in range(8):
                                        if ((i,j),(a,b)) in pojej:
                                                sez_vseh_iz_pozicije.append(((i,j),(a,b)))
                                                self.kanvas.create_rectangle(i*100 - 50,i*100 + 50,
                                                    i*100 - 50,i*100 + 50,

                                                outline="#000000", fill="#1020FF")
                print((i,j))
                print(sez_vseh_iz_pozicije)
                if sez_vseh_iz_pozicije != []:
                        self.kanvas.unbind("<Button-1>")
                        self.kanvas.bind("<Button-1>", self.kanvas_klik2)
                return sez_vseh_iz_pozicije

                       ##problem: retturn ne sme bit seznam, ampak klik!
#naslednji cilj: zdru�itev obeh klikov, oba morta vrnt neki

                                          
                

        def kanvas_klik2(self,event2):
        # dobiva nove koordinate in narediva potezo ce je med veljavnim
                klik1 = [((2,2),(3,3))] #neka cifra za poskus
                if klik1 == []:
                        pass
                i = event2.x // 100
                j = event2.y // 100
                for (a,b),(c,d) in klik1:
                         if (c,d) == (i,j):
                                self.igra.na_potezi.klik(((a,b),(c,d)))
                                print("pridem do sem")
                                self.kanvas.unbind("<Button-1>")
                                self.kanvas.bind("<Button-1>", self.kanvas_klik1)
                         else:
                                pass
                print("NEKI")

        def naredi_potezo(self,a,p):
        # a so stare koordinate, ki jih dobimo s klikom, p pa nove
                igralec = self.igra.na_potezi
                self.igra.naredi_potezo(a,p)

                
                
                        
                        
                        
        

        
            
            


 #GLAVNI PROGRAM
root = Tk()
root.title("Dama")
aplikacija = Gui(root)
root.mainloop()

