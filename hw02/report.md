## První část

### Fitness a selekce
Používal jsem tournament selection i roulette wheel selection.

Fitness jsem použil pouze předem dodanou. Zkoušel jsem exponenciální, ale floating pointy příliš nesouhlasily.
Záporný objective jsem nepoužíval, jelikož pro roulette wheel selection nemá cenu a pro tournament selection dopadne stejně jako default.

### Hyperparametry
Napište, jaké nastavení hyperparametrů jste použili (velikost populace, pravděpodobnost mutace, pravděpodobnost křížení, počet generací).
Uveďte, zda jste zkoušeli různé hodnoty a jaký to mělo vliv na běh algoritmu.

Zkoušel jsem různé hodnoty pro crossover i pro mutace, také jsem měnil počty jedinců a generací. 
Počet generací příliš velký vliv neměl (zkoušel jsem zvětšovat), počet jedinců taky zas tak velký ne
(nejmenší počet jsem zkusil 50).

Zvětšování pravděpodobností mutace (u flip mutace) vedlo k menší stabilitě,
crossoverem jsem zvětšoval, ale příliš velký vliv to nemělo.

### Nejlepší výsledek
Jakého nejlepšího výsledku jste dosáhli? S jakým nastavením?

## Druhá část

### Použité operátory
Popište, jaké chytré operátory jste implementovali. Pokud jsou to některé ze standardních zmiňovaných na cvičení, stačí zase jen název.

### Hyperparametry
Jaké nastavení hyperparametrů jste použili?

## Závěr pro obě části

Co jste zjistili? Co fungovalo nejlépe a proč? Porovnejte výsledky obou částí (Stačí pár vět.) Nezapomeňte přiložit grafy s průběhem fitness. Obě části můžete porovnat v jednom obrázku (pokud je přehledný).

## Použití generativní AI

Uveďte, zda a jak jste při práci na úkolu použili generativní AI (např. ChatGPT, Copilot). Pokud jste ji nepoužili, napište to.
