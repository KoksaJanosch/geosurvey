import csv

# Načte data jako "csvfile", oddělí podle ";"
with open ("test_data.csv", encoding='utf-8-sig') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=";")

    for row in readCSV:
        rows = row
        print(rows)

    # readRow1 = next(readCSV)
    # print(readRow1)


if "Věk" in rows[0]:
    print("Věk na indexu: ", rows.index("Věk"))
    rows = [item.replace("Věk", "Věk nový") for item in rows]
    print(rows)
else:
    print("HP.")

    # vypiš kolik má seznam prvků
    # vypiš kolik prvků se nahradilo

