text = "Slon je modrý. Má telefon: jeho telefon je 555. Je hezký, všichni návštěvníci ho mají rádi. Je z Afriky; mohl by být i z Indie. Náš slon se jmenuje slono.bobo."

import re

muj_regex = re.compile(r"[;,:.]\s")

roztrhany_text = muj_regex.split(text)

print(roztrhany_text)

