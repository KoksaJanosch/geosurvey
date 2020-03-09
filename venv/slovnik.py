
# načti vstupní soubor
# rozparceluj ho na slovník
# najdi ze vstupu "slovo", nahraď slovem ze vstupu

import csv
import os
from pathlib import Path

# cesta k souborům
data_folder = Path("data/")

inputFile_vzor = data_folder / "vzor.csv"   # načti vzor

# nastavení parametrů "inputu" a "outputu"
with open(inputFile_vzor, newline='', encoding='utf-8-sig') as inVzor:
    r = csv.reader(inVzor, delimiter=";")

    # získá první řádek "vzoru"
    rowHeader_vzor = next(r)
    # vypíše hlavičku a data "vzoru"
    print("hlavička_vzor:", rowHeader_vzor)
    # vypíše zbytek dat
    for row in r:
        print("hodnota_vzor:", row)

    dictionary = dict(zip(rowHeader_vzor, row))
    print(dictionary)
