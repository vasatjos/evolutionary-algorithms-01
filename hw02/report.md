## První část

### Fitness a selekce
Používal jsem tournament selection i roulette wheel selection.

Fitness jsem použil pouze předem dodanou. Zkoušel jsem exponenciální, ale floating pointy příliš nesouhlasily.
Záporný objective jsem nepoužíval, jelikož pro roulette wheel selection nemá cenu a pro tournament selection dopadne stejně jako default.

### Hyperparametry

Číselné hodnoty hyperparametrů jsem zkoušel ve všelijakých kombinacích, většina
výsledků mi ale nepřišla příliš zajímavá. K perfektnímu skóre jsem se příliš nepřiblížil...

Věci co konzistentně zlepšily výsledek byla menší pravděpodobnost flipu při mutaci,
tournament selection, která porážela ruletovou a elitismus taky vedl k lepším výsledkům
(zkoušel jsem pouze velikost elity 1).


### Nejlepší výsledek

Nejlepší běh měl největší rozdíl 173 s následujícím nastavením (tournament selection):

```python
POP_SIZE = 100  # population size
MAX_GEN = 1000  # maximum number of generations
CX_PROB = 0.8  # crossover probability
MUT_PROB = 0.5  # mutation probability
MUT_FLIP_PROB = 0.007  # probability of chaninging value during mutation
ELITISM = True
```

## Druhá část

### Použité operátory

Zkoušel jsem uniform i 2-point crossovery, oba se zdáli horší.
Zkoušel jsem také kombinaci všech 3 crossoverů, ale ačkoliv fungovalo,
standardní 1-point byl nejlepší.

Dále jsem zkusil použít swap mutaci, která byla kupodivu horší než jen flip.
Nejzajímavější byly greedy mutace, kde obyčejná přesunula náhodný prvek z nejtěžšího
bucketu do nejlehčího, a greedy swap prohodil náhodné prvky v těchto bucketech.


### Hyperparametry

Opět jsem použil tournament selection, s mutací greedy_swap jsem dosáhl perfektního
skóre.
```python
POP_SIZE = 100  # population size
MAX_GEN = 1000  # maximum number of generations
CX_PROB = 0.8  # crossover probability
MUT_PROB = 0.2  # mutation probability
MUT_FLIP_PROB = 0.01  # probability of chaninging value during mutation
ELITISM = True
```

## Závěr pro obě části

Elitismus razantně zlepšuje konvergenci. Tuším že je to náročností problému, a tedy se vyplácí nezahazovat nějaké dobré řešení.
Tournament selection je lepší než ruletová. Tady se přiznám že nevidím jasný důvod, proč by měla vyhrávat, ale experimenty mluví jasně.

Greedy mutace na plné čáře válcuje bit flip, nebo dokonce i prohození. Předpokládám že je to tím, že je mutace hodně specifická
pro doménu, a chytře využívá informaci o ní, kterou jednodušší mutace nemají. Zároveň není kompletně náhodná, takže oproti
obyčejným mutacím v podstatě "podvádí".

## Použití generativní AI

Použil jsem pouze pro generování krátkých funkcí ("napiš za mě greedy mutaci", "napiš za mě uniform crossover" atd.)
