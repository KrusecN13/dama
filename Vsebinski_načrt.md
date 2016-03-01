# Vsebinski načrt: <h1>
Program je napisan s programom Python 3, njegov uporabniški vmesik pa uporablja knjižnico Tkinter.

## Pravila igre: <h2>

#### Igralno polje: <h4>

* Igramo na šahovnici, velikosti 8 x 8 s črnimi in belimi polji, figure so postavljene samo na črna polja prvih treh stolpcev na strani vsakega igralca. Vsak igralec ima torej 12 figur, nekdo bele, drugi pa črne barve.

#### Potek igre: <h4>

* Prvo potezo izvede igralec s črnimi figurami
* Običajne figure se premikajo diagonalno naprej
* Če je figura drugega igralca na sosednjem diagonalnem polju v smeri nasprotnika, in je diagonalno za njim prazno polje, potem lahko to figuro 'poješ', kar pomeni: lastno figuro pa premakneš za dve diagonalni polji naprej v smeri, kjer si pojedel nasprotnikovo figuro, to pa odstraniš z igralnega polja
* Če z lastno figuro prideš do drugega konca igralnega polja, tvoja figura postane dama. Ta se sme premikati in jesti tudi diagonalno nazaj

#### Pogoj za zmago: <h4>

* Igralec zmaga, ko poje nasprotniku vse figure oziroma nasprotniku prepreči izvedbo katerekoli poteze. Vedno je nekdo zmagovalec, izenačenja ni.

## Razredi: <h2>

#### Razred GUI: <h4>
Vmesnik bo vseboval metode, s katerimi bo risal poteze na platno. Celotni razred skupaj z metodami bo vsebovan v (glavni) datoteki dama.py. Uporabljene metode bodo:
* izbira_igralca(self)
* zacni_igro(self)
* premakni_figuro(self,i,j)
* koncaj_igro(self, zmagovalec)

#### Igralci in njihovi razredi: <h4>
Igra proti računalniku bo vsebovala dva algoritma, enega namerno neizpopolnjenega in lažjega (Minimax) in pa bolj dodelanega (alfa-beta rezanje). Tretja možnost je, da je igralec človek, v tem primeru mu podelimo možnost izvajanja poteze preko uporabniškega vmesnika. Razredi igralcev bodo:
* class Minimax 
* class Alfa_beta
* class clovek, ki bo imel metodi:
    * __init__(self, gui), ki se bo povezala z uporabniškim vmesnikom, 
    * premakni(self)

#### Razred Igra: <h4>
Metode znotraj razreda Igra bodo:
* naredi_potezo(self,i,j), ki se bo razdelila na podmetodi premakni(self,i,j) in pojej(self,i,j)
* razveljavi(self)
* na_potezi(self)
* je_veljavna(self,i,j)
* zmagovalec(self)







