import os, sys, csv
from pathlib import Path

# cesta k souborům
cesta_data = Path("data/")

in_vzor = cesta_data / "vzor.csv"
in_file = cesta_data / "test_data.csv"
out_file = os.path.splitext(in_file)[0] + "_completed.csv"

# Funkce: hlavičky z inputů
with open(in_vzor, newline='', encoding='utf-8-sig') as in_slovnik, \
     open(in_file, newline='', encoding='utf-8-sig') as in_data:

    r_slovnik = csv.reader(in_slovnik, delimiter=";")
    r_data = csv.reader(in_data, delimiter=";")

    # Slovník: klíče (hlavička), hodnoty
    header_slovnik = next(r_slovnik)    # získá hlavička
    for rows_s in r_slovnik:    # získá hodnoty ke klíčům
        row_slovik = (rows_s)
    slovnik = dict(zip(header_slovnik, row_slovik)) # vytvoří slovník
    print("slovnik:", slovnik)

    header_data = next(r_data)  # získá hlavičku
    print("data:", header_data)
    for data_r in r_data:
        data = (data_r)
    header_dataOut = header_data
print("\n")

for klic_slovnik in header_slovnik:
    # print("hledám pro:", klic_slovnik)
    for klic_data in header_data:
        if klic_slovnik == klic_data:
            # print("ANO", klic_data)
            value_slovnik = slovnik.get(klic_slovnik)
            header_dataOut = [value_data.replace(klic_data, value_slovnik) for value_data in header_dataOut]
        else:
            # print("nenalezena shoda:", klic_data)
            pass

# "output" file
with open(out_file, 'w', newline='', encoding='utf-8-sig') as out_data:
    w_data = csv.writer(out_data, delimiter=";")

    # zapíše
    w_data.writerow(header_dataOut)
    w_data.writerow(data)

def Diff(li1, li2):
    return (list(set(li1) & set(li2)))

print("Nezměněno:", Diff(header_dataOut, header_data))


# dirs = os.listdir(cesta_data)
# for file in dirs:
#     print(file)


