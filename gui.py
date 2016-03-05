###### Razred GUI: <h4>
##Vmesnik bo vseboval metode, s katerimi bo risal poteze na platno.
#Celotni razred skupaj z metodami bo vsebovan v (glavni) datoteki dama.py.


from Tkinter import *
#import dama
#Definiramo razred, ki predstavlja našo aplikacijo
class Gui():
        def __init__(self, master=None):
            #init = stvari ki se zgodijo enkrat, vse kar se more zgodit, da
            #zaženemo grafièni vmesnik

            self.canvas = Canvas(master, width=1000, height=800)
            self.canvas.pack()
            for x in range(0,800,100):
                for y in range(0,800,100):
                    if ((x+y)//100)%2 == 0:
                       self.canvas.create_rectangle(x+(100),y+(100),
                                                    x,y,
                                                    outline="#000000", fill="#000000")

                    else:
                       self.canvas.create_rectangle(x+(100),y+(100),
                                                    x,y,
                                                    outline="#ffffff", fill="#ffffff")
##          self.beli = Button(master, text="beli") 
##          for x in range(125/2,1000, 125):
##              for y in range(125/2,250 + 125/2, 125):
##                  if (x+y) % 2 == 0:
##                    self.beli.grid(row=x, column=y)
##             
##          self.pozdrav = StringVar(master, value="DAMA")     
##          Label(master, textvariable=self.pozdrav).grid(row=900, column=50)
                    
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
aplikacija = Gui()
root.mainloop()
# more bit Gui(root), sam piÅ¡e da nima argumentov
