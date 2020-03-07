
# načti vstupní soubor
# rozparceluj ho na slovník
# najdi ze vstupu "slovo", nahraď slovem ze vstupu

import csv
import os
from pathlib import Path

# cesta k souborům
data_folder = Path("data/")

inputFile_vzor = data_folder / "vzor.csv"   # načti vzor
inputFile_input = data_folder / "test_data.csv"  # načti "input"

# nastavení parametrů "inputu" a "outputu"
with open(inputFile_vzor, newline='', encoding='utf-8-sig') as inVzor, \
     open(inputFile_input, newline='', encoding='utf-8-sig') as inInput:
    r = csv.reader(inVzor, delimiter=";")
    r2 = csv.reader(inInput, delimiter=";")


    # získá první řádek, jestli je "hodnota1", nahraď "hodnota2"
    rowHeader_vzor = next(r)

    # vypíše hlavičku a data "vzoru"
    print("hlavička_vzor:", rowHeader_vzor)
    # vypíše zbytek dat
    for row in r:
        print("data_vzor:", row)

    # vypíše hlavičku "inputu"
    rowHeader_input = next(r2)
    print("hlavička_input", rowHeader_input)

# když bude HEADER_VZOR = HEADER_INPUT
for idx, prvekRow_vzor in enumerate(rowHeader_vzor):
    a = prvekRow_vzor

for prvekRow_input in rowHeader_input:
    print(a)
    if a == prvekRow_input:
        print(prvekRow_vzor, "- SHODA")
    else:
        print(prvekRow_input, "- není shodný")

