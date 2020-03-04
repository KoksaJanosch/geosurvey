# vyčte pouze první řádek
readRow1 = next(readCSV)
print(readRow1)


# funkční

if "Věk" in readRow1:
    print("Věk na indexu: ", readRow1.index("Věk"))
    readCSV = [item.replace("Věk", "Věk nový") for item in readRow1]
    print(readCSV)
else:
    print("HP.")



# Načte data jako "csvfile", oddělí podle ";"
with open ("test_data.csv", encoding='utf-8-sig') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=";")

    for row in readCSV:
        rows = row
        print(rows)
