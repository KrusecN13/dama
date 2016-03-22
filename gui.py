###### Razred GUI: <h4>
##Vmesnik bo vseboval metode, s katerimi bo risal poteze na platno
#Celotni razred skupaj z metodami bo vsebovan v (glavni) datoteki dama.py.


from Tkinter import *
from dama import *

#Definiramo razred, ki predstavlja našo aplikacijo
class Gui():
        def __init__(self, master=None):
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
                zapri_menu.add_command(label = "Izhod", command = master.destroy)

                self.canvas = Canvas(master, width=800, height=800)
                self.canvas.grid()

                self.napis = StringVar(master, value = "Dama")
                Label(master, textvariable = self.napis, background = 'orange').grid(row=1, column=0)



                self.ime_igralcaC = StringVar(master, value = 'Crni igralec')
                self.ime_igralcaB = StringVar(master, value = 'Beli igralec')
                canvas_ime_igralcaC = Entry(master, width = 10, textvariable = self.ime_igralcaC, background = 'orange')
                canvas_ime_igralcaB = Entry(master, width = 10, textvariable = self.ime_igralcaB, background = 'orange')
                canvas_ime_igralcaC.grid()
                canvas_ime_igralcaB.grid()

                slovar_figur = {}
                for x in range(0,800,100):
                        for y in range(0,800,100):
                                if ((x+y)//100)%2 == 0:
                                        self.canvas.create_rectangle(x+(100),y+(100),
                                                    x,y,
                                                    outline="#000000", fill="#000000")

                                else:
                                       self.canvas.create_rectangle(x+(100),y+(100),
                                                    x,y,
                                                    outline="#ffffff", fill="#CD8527")
                for i in range(8):
                        for j in range(3):
                                if (i+j)%2 == 0:
                                        a = self.canvas.create_oval(i*100 + 15, j*100 + 15, i*100 + 85, j*100 + 85, fill='#7D26D9', outline='#000000') 
                                        slovar_figur[Figura('igrC')]=a
                for i in range(8):
                        for j in range(5,8):
                                if (i+j)%2 == 0:
                                        a = self.canvas.create_oval(i*100 + 15, j*100 + 15, i*100 + 85, j*100 + 85, fill='#9EB5BA', outline='#000000') 
                                        slovar_figur[Figura('igrB')]=a
                                        
                print(slovar_figur)
##          na koncu inita: izbira igralcev (veže na funkcijo izbira_igralca,
##          ta dela naprej)
        
        def premakni_figuro(self,i,j):
            pass

        def izbira_igralca(self):
            pass

        def zacni_igro(self):
            pass

        def koncaj_igro(self,zmagovalec):
            pass
            
            


 #GLAVNI PROGRAM
root = Tk()
root.title("Dama")
aplikacija = Gui(root)
root.mainloop()

