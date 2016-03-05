###### Razred GUI: <h4>
##Vmesnik bo vseboval metode, s katerimi bo risal poteze na platno. Celotni razred skupaj z metodami bo vsebovan v (glavni) datoteki dama.py. Uporabljene metode bodo:
##* izbira_igralca(self)
##* zacni_igro(self)
##* premakni_figuro(self,i,j)
##* koncaj_igro(self, zmagovalec)
##

from Tkinter import *
#import dama
#Definiramo razred, ki predstavlja naöo aplikacijo
class Gui(Frame):
       def __init__(self, master=None):
            Frame.__init__(self,master)
            self.pack #funkcija, ki izraËuna velikost okna
            self.createWidgets
            pass
        
       def createWidgets(self):
            self.polje = tk.Button(self)#naredi gumb
            self.polje["command"] = self.premakni ## premakni bo funkcija iz kode,
            ##ki bo premaknila figuro, vsakic ko se gumb pritisne se sproûi funkcija
##            self.polje.pack(side=## kje vse morajo bit gumbi?
##            self.Igraj = tk.Button(self, text = "Igraj novo!", fg="blue",
##                                   command=root.#razveljavitev celotne igre
##                                   ##in zaËetek nove
##
##            self.Quit = tk.Button(self, text = "KonËaj igro", fg="red",
##                                  command=root.destroy)
##            self.Quit.pack(side= ##kjer bo gumb za konec"
##
##    # igralno obmoƒçje
##            self.deska = tkinter.Canvas(master, width=500, height=500)
##            self.deska.grid(row=1,column=1)
##            
              

#GLAVNI PROGRAM
root = Tk()
root.title("Dama")
aplikacija = Gui()
root.mainloop()## JURE: si zihr, da je root.mainloop, al ni aplikacija.mainloop? :)
# more bit Gui(root), sam pi≈°e da nima argumentov
