## Použité operátory

Ruletová selekce, 1-point crossover, bit flip mutace. Elitismus ani tournament selection jsem nezkoušel. (Příští úkol zkusím nenechat na poslední chvíli, nejspíš by z toho byly zajímavější grafy.)

## Fitness pro střídající se jedničky a nuly

Použil jsem následující fitness: `fitness += individual[i] != individual[i + 1]`, tedy s maximální hodnotou 24.

## Vyzkoušené změny hyperparametrů

Zkoušel jsem změny pravděpodobností pro crossover, mutaci a bit-flipu při mutaci.
Crossover skoro neměl vliv, 0.5 zkonvergovala rychle, 0.8 taky, 0.9 nenašla maximum, 0.99 zase ano a rychle.
Pravděpodobnost mutace při snížení zpomalila konvergenci, při zvýšení způsobovala výkyvy. Těm by se možná dalo částečně zamezit elitismem.
Pravděpodobnost bit flipu byla při odchylce od průměrně jedné změny vždy horší.

## Závěr

Nejlépe fungovaly následující hodnoty:
```python
CROSSOVER_PROB = 0.99
MUTATION_PROB = 0.1
MUTATION_FLIP_PROB = 1 / INDIVIDUAL_LENGTH
```
Ale určitě existuje i nějaké varianta kterou jsem nezkusil.
Jak jsem již psal, 0.8 CROSSOVER_PROB maximum fitness našla a 0.9 už zase ne,
ale zbývající dvě hodnoty se takto jeví jako nejrozumnější.

## Použití generativní AI
 
Použil jsem pouze jako fancy náhradu Stack Overflow (rady ohledně `matplotlib` syntaxe atd.).
