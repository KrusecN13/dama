# Pravila igre: <h1>

## Igralno polje: <h2>

* Igramo na šahovnici, velikosti 8 x 8 s črnimi in belimi polji, figure so postavljene samo na črnih poljih prvih treh stolpcev na strani vsakega igralca. Vsak igralec ima torej 12 figur, nekdo bele, drugi pa črne barve.

## Potek igre: <h2>

* Prvo potezo izvede igralec s črnimi figurami
* Običajne figure se premikajo diagonalno naprej
* Če je figura drugega igralca na sosednjem diagonalnem polju v smeri nasprotnika, in je diagonalno za njim prazno polje, potem lahko to figuro 'poješ', kar pomeni: lastno figuro pa premakneš za dve diagonalni polji naprej v smeri, kjer si pojedel nasprotnikovo figuro, to pa odstraniš z igralnega polja
* Če z lastno figuro prideš do drugega konca igralnega polja, tvoja figura postane dama. Ta se sme premikati in jesti tudi diagonalno nazaj

## Pogoj za zmago: <h2>

* Igralec zmaga, ko poje nasprotniku vse figure oziroma nasprotniku prepreči izvedbo katerekoli poteze. Vedno je nekdo zmagovalec, izenačenja ni.

## Struktura programa:

## Razredi: <h2>

## Metode uporabniškega vmesnika GUI: <h2>
Vmesnik bo vseboval metode, s katerimi bo risal poteze na ploščo:
igralec_na_potezi(self) 
začni_igro(self) 
nariši_potezo(self,i,j)
koncaj(self,z)

## Igralci in njihovi razredi <h2>
Igra proti računalniku bo vsebovala dva algoritma, enega namerno neizpopolnjenega in lažjega (Minimax) in pa bolj dodelanega (alfa-beta rezanje). Tretja možnost je, da je igralec človek, v tem primeru mu podelimo možnost izvajanja poteze prek uporabniškega vmesnika.
* class Minimax 
* class Alfa_beta
* class clovek
__init__(self, gui) 
povleci(self)

## Splošna struktura igre: <h2>
* class Igra
premakni_ali_pojej(self,i,j)
(self,i,j)
razveljavi(self)
na_potezi(self)
veljavnost_poteze(self)
vse_veljavne(self)
zmagovalec(self)







