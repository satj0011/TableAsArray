Generella krav för implementationer
Krav för alla implementationer av datatypen tabell
Gränsytan som implementeras ska följa detta exempel(TableAsArray) Ladda ner detta exempelexakt och får inte ändras.
Ett tips är att ladda hem filen och ha den som utgångspunkt när du implementerar TableAsArray.
Dubbletter måste hanteras:
En tabell får endast innehålla ett värde per nyckel. D.v.s, det får inte, utifrån sett, finnas dubbletter av nycklar i tabellen.
Däremot finns inget krav på att tabellen inte får lagra flera värden per nyckel, så länge det är osynligt för användaren.

Detta ger oss två alternativ att välja på:
Hantera dubbletter vid insättning:
Om nyckeln redan finns i tabellen skrivs det tidigare associerade värdet över med det nya.
Hantera dubbletter vid uppslagning och borttagning:
Låt lookup alltid returnera det senast tillagda objektet asssocierat med en nyckel. 
Låt remove ta bort alla objekt associerade med den nyckel som ska tas bort.
Tidskomplexitet:
Tidskomplexiteten för att svara på om tabellen är tom ska vara O(1).
Funktionerna insert, lookup och remove får maximalt kosta O(n) där n är antal element som finns lagrade i tabellen. 
Till exempel räcker det inte med O(m) om m är maximalt antal element i arrayen.
