# Token generator for Bakalari API
Jednoduchý Python script pro vygenerování tokenu pro Bakaláři API.

Doporučuji: [xmlcurl](https://github.com/mariansam/xmlcurl)

Dependencies:
- Python 2.7

## Návod
Script chce tři argumenty - doménu serveru Bakalářů, uživatelské jméno, heslo. Příklad:
```sh
./mktoken.py bakalari.gjp-me.cz jannovak honzovosilnyheslo
```

Skript vždy vygeneruje token ke dnešnímu datu.
