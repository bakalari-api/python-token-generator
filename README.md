# Token generator for Bakalari API
Jednoduchý Python script pro vygenerování tokenu pro Bakaláři API.

Doporučuji: [xmlcurl](https://github.com/mariansam/scripts/tree/master/xmlcurl)

## Návod
Skript vyžaduje tři argumenty - adresu serveru Bakalářů, uživatelské jméno, heslo.

Pokud použijete argument `-k/--keep-url`, adresa by měla vypadat zhruba takto:  
`https://subdomena.skola.cz/bakalari/login.aspx`

Tedy včetně protokolu (`https://`) a `/login.aspx`, ale bez `/next/` (pokud vaše škola
používá tuto verzi rozhraní) a bez query stringu (`?neco=neco...`).

Pokud `-k` použijete, skript se pokusí adresu upravit. Nejkratší formát, který
vygeneruje stejnou adresu jako výše, je `subdomena.skola.cz/bakalari`.

Vygenerovaný token je platný vždy pouze k danému datu

### Python 2
Not supported anymore, if you're really that **boomer**, checkout commit
[`c555ec1`](https://github.com/bakalari-api/python-token-generator/tree/c555ec15e7a767ebd55c9a3022a07d4633977fcd).

### Python 3

#### Z příkazového řádku

```
použití: bakalari_token.py [-h] [-k] url username [pwd]

poziční argumenty:
  url             URL Bakalářů (např. subdomena.skola.cz/bakalari)
  username        Uživatelské jméno
  pwd             Heslo (volitelné, pokud nezadáno, bude vyžádáno schovaným vstupem)

volitelné argumenty:
  -h, --help      Zobrazí tuto nápovědu a ukončí program
  -k, --keep-url  Nepokoušet se upravit URL. URL by tedy už mělo být něco jako https://subdomena.skola.cz/bakalari/login.aspx
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
if not is_full_url:
    url = bakalari_token.process_url(url)
token = bakalari_token.generate_token(url, "jannovak", "honzovosilnyheslo")
```
