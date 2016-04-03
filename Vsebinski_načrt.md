# Vsebinski načrt: <h1>
Program je napisan s programom Python 3, njegov uporabniški vmesik pa uporablja knjižnico Tkinter.

## Pravila igre: <h2>

#### Igralno polje: <h4>

* Igramo na šahovnici, velikosti 8 x 8 s črnimi in belimi polji, figure so postavljene samo na črna polja prvih treh stolpcev na strani vsakega igralca. Vsak igralec ima torej 12 figur, nekdo bele, drugi pa črne barve.

#### Potek igre: <h4>

* Prvo potezo izvede igralec s črnimi figurami
* Običajne figure se premikajo diagonalno naprej
* Če je figura drugega igralca na sosednjem diagonalnem polju v smeri nasprotnika, in je diagonalno za njim prazno polje, potem lahko to figuro 'poješ', kar pomeni: lastno figuro premakneš za dve diagonalni polji naprej v smeri, kjer si pojedel nasprotnikovo figuro, to pa odstraniš z igralnega polja
* Če z lastno figuro prideš do drugega konca igralnega polja, tvoja figura postane dama. Ta se sme premikati in jesti tudi diagonalno nazaj

#### Pogoj za zmago: <h4>

* Igralec zmaga, ko poje nasprotniku vse figure oziroma nasprotniku prepreči izvedbo katerekoli poteze. Vedno je nekdo zmagovalec, izenačenja ni.

## Razredi: <h2>

#### Razred GUI: <h4>
Vmesnik bo vseboval metode, s katerimi bo risal poteze na platno. Celotni razred skupaj z metodami bo vsebovan v (glavni) datoteki gui.py. Uporabljene metode bodo:
* zacni_igro(self, igrc, igrb)
* postavi_figure(self)
* naredi_potezo(self)
* koncaj_igro(self, zmagovalec)
* izhod(self)

#### Igralci in njihovi razredi: <h4>
Igra proti računalniku bo vsebovala tri algoritme, enega namerno neizpopolnjenega in lažjega (Random) in pa bolj dodelana (Minimax in Alpha-beta). Tretja možnost je, da je igralec človek, v tem primeru mu podelimo možnost izvajanja poteze preko uporabniškega vmesnika. Uporabljeni razredi bodo:

* class Figura, ki ima objekte figure z določeno barvo ter značilnostjo dama.
* class Racunalnik in class Clovek z metodami: init(self, gui), igraj(self), prekini(self), klik(self, p) in za class Racunalnik še metoda preveri(self).
* class Minimax
* class Random
* class Alpha_beta

#### Razred Igra: <h4>
Metode znotraj razreda Igra bodo:
* naredi_potezo(self,i,j),
* stanje_igre(self),
* veljavne_poteze(self, igralec)







