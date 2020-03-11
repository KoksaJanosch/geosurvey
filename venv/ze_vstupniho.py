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


    # získá první řádek "vzoru"
    rowHeader_vzor = next(r)
    # vypíše hlavičku a data "vzoru"
    print("hlavička_vzor:", rowHeader_vzor)
    # vypíše zbytek dat
    for row in r:
        print("hodnota_vzor:", row)
    # vytvoří slovník ze "vzoru"
    dictionary = dict(zip(rowHeader_vzor, row))
    print("slovník ze vzoru:", dictionary)
    
    # vypíše hlavičku "inputu"
    rowHeader_input = next(r2)
    print("hlavička_input", rowHeader_input)
    print("\n")


# když bude HEADER_VZOR = HEADER_INPUT
for prvekRow_vzor in rowHeader_vzor:
    print("hledám pro prvek:", prvekRow_vzor)
    for prvekRow_input in rowHeader_input:
        if prvekRow_vzor == prvekRow_input:
            print(prvekRow_input, "- SHODA")
            # získej dvojíci ze "slovníku"
            dvojice_slovnik = dictionary.get(prvekRow_vzor)
            print("NAHRADÍM: ", dvojice_slovnik)

        else:
            print(prvekRow_input, "- není shodný")
    print("\n")

