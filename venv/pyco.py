import csv
import os
from pathlib import Path

# cesta k souborům
cesta_data = Path("data/")

in_vzor = cesta_data / "vzor.csv"
in_file = cesta_data / "test_data.csv"
out_file = os.path.splitext(in_file)[0] + "_completed.csv"

# nastavení parametrů "inputu" a "outputu"
with open(in_vzor, newline='', encoding='utf-8-sig') as in_slovnik, \
     open(in_file, newline='', encoding='utf-8-sig') as in_data, \
     open(out_file, 'w', newline='', encoding='utf-8-sig') as out_data:

    r = csv.reader(in_slovnik, delimiter=";")
    r2 = csv.reader(in_data, delimiter=";")
    w = csv.writer(out_data, delimiter=";")


    