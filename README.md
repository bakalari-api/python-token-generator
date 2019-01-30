# Token generator for Bakalari API
Jednoduchý Python script pro vygenerování tokenu pro Bakaláři API.

Doporučuji: [xmlcurl](https://github.com/mariansam/xmlcurl)

## Návod
Script chce tři argumenty - doménu serveru Bakalářů, uživatelské jméno, heslo. Příklad:
Python 2:
```sh
./mktoken.py bakalari.gjp-me.cz jannovak honzovosilnyheslo
```

Python 3:
```sh
./mktoken3.py bakalari.gjp-me.cz jannovak honzovosilnyheslo
```

Skript vždy vygeneruje token ke dnešnímu datu.
