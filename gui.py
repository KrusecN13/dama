###### Razred GUI: <h4>
##Vmesnik bo vseboval metode, s katerimi bo risal poteze na platno.
#Celotni razred skupaj z metodami bo vsebovan v (glavni) datoteki dama.py.
#Uporabljene metode bodo:
##* izbira_igralca(self)
##* zacni_igro(self)
##* premakni_figuro(self,i,j)
##* koncaj_igro(self, zmagovalec)
##

from Tkinter import *
#import dama
#Definiramo razred, ki predstavlja našo aplikacijo
class Plosca():
        def __init__(self, master=None):
           self.canvas = Canvas(master, width=1000, height=1000)
           self.canvas.pack()
           for x in range(0,1000,125):
               for y in range(0,1000,125):
                   if (x+y) % 2 == 0:
                       self.canvas.create_rectangle(x+125,y+125,
                                                    x,y,
                                                    outline="#000000", fill="#000000")

                   else:
                       self.canvas.create_rectangle(x+125,y+125,
                                                    x,y,
                                                    outline="#ffffff", fill="#ffffff")
##           self.beli = Button(master, text="beli") 
##           for x in range(125/2,1000, 125):
##                for y in range(125/2,250 + 125/2, 125):
##                     if (x+y) % 2 == 0:
##                         self.beli.grid(row=x, column=y)
##       ta del še ne dela                  
                    
                    

        #naredi šahovsko plošèo
        def premakni(self):
           pass
            
            


 #GLAVNI PROGRAM
root = Tk()
root.title("Dama")
aplikacija = Plosca()
root.mainloop()
# more bit Gui(root), sam piÅ¡e da nima argumentov
