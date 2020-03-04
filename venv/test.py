import csv
import os

inputFileName = "test_data.csv"
outputFileName = os.path.splitext(inputFileName)[0] + "_modified.csv"

with open(inputFileName, newline='', encoding='utf-8-sig') as inFile, open(outputFileName, 'w', newline='', encoding='utf-8-sig') as outfile:
    r = csv.reader(inFile, delimiter=";")
    w = csv.writer(outfile, delimiter=";")

    # získá první řádek
    row1 = next(r)
    # jestli je "hodnota1", nahraď "hodnota2"
    row1 = [item.replace("Věk", "XXX") for item in row1]
    row1 = [item.replace("Jméno", "YYY") for item in row1]
    print(row1)
    for row in r:
        print(row)  # nahradit w.writerow




    # # přeskočí/přepíše původní hlavičku
    # next(r, None)
    # # napíše novou hlavičku
    # w.writerow(['Item Number', 'Item Description', 'List Price', 'QTY Available'])
    #
    # # zkopíruje zbytek
    # for row in r:
    #     w.writerow(row)