import os, sys, csv
from pathlib import Path

# cesta k souborům
cesta_data = Path("data/")

in_uziv = cesta_data / [input("název souboru: ") + ".csv"]
print(in_uziv)




print(in_vzor)