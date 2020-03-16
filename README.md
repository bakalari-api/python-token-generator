# Token generator for Bakalari API
Jednoduchý Python script pro vygenerování tokenu pro Bakaláři API.

Doporučuji: [xmlcurl](https://github.com/mariansam/scripts/tree/master/xmlcurl)

## Návod
Skript vyžaduje tři argumenty - adresu serveru Bakalářů, uživatelské jméno, heslo.

Adresu uvádějte bez `https://` a bez `/login.aspx`, případně i bez `/next/`,
pokud vaše škola tuto verzi rozhraní Bakalářů používá.  
_Příklad_: Pokud na se na vaše Bakaláře přihlašujete na stránce
`https://subdomena.skola.cz/bakalari/next/login.aspx`,
tak jako adresu uveďte `subdomena.skola.cz/bakalari`.

Vygenerovaný token je platný vždy pouze k danému datu

### Python 2
Not supported anymore, if you're really that **boomer**, checkout commit
[`c555ec1`](https://github.com/bakalari-api/python-token-generator/tree/c555ec15e7a767ebd55c9a3022a07d4633977fcd).

### Python 3

#### Z příkazového řádku

```
použití: bakalari_token.py [-h] url username [pwd]

poziční argumenty:
  url         URL Bakalářů (např. subdomena.skola.cz/bakalari)
  username    Uživatelské jméno
  pwd         Heslo (volitelné, pokud nezadáno, bude vyžádáno schovaným vstupem)

volitelné argumenty:
  -h, --help  Zobrazí tuto nápovědu a ukončí program
```

##### Použití skriptu přímo
```sh
git clone https://github.com/bakalari-api/python-token-generator.git
cd python-token-generator
./bakalari_token.py <argumenty>
```

##### Instalace
```sh
python3 -m pip install bakalari-token
bakalari-token <argumenty>
```

#### Použití jako modul
```python
import bakalari_token
token = bakalari_token.generate_token("subdomena.skola.cz/bakalari", "jannovak", "honzovosilnyheslo")
```
