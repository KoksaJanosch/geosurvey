import csv
import os
from pathlib import Path

# cesta k souborům
data_folder = Path("data/")

# proměnné "input" a "output" souborů
inputFileName = data_folder / "test_data.csv"
outputFileName = os.path.splitext(inputFileName)[0] + "_completed.csv"

# nastavení parametrů "inputu" a "outputu"
with open(inputFileName, newline='', encoding='utf-8-sig') as inFile, open(outputFileName, 'w', newline='', encoding='utf-8-sig') as outfile:
    r = csv.reader(inFile, delimiter=";")
    w = csv.writer(outfile, delimiter=";")

    # získá první řádek, jestli je "hodnota1", nahraď "hodnota2"
    row1 = next(r)
    row1 = [item.replace("Věk", "XXX") for item in row1]
    row1 = [item.replace("Jméno", "YYY") for item in row1]

    # vypíše hlavičku a data
    print("hlavička:", row1)
    w.writerow(row1)
    for row in r:
        print("data:", row)
        w.writerow(row)
