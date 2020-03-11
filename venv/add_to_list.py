list = ["Jméno", "Věk", "Chyna", "Pes"]
slovnik_header = ["Jméno", "Věk", "Pes"]
slovnik = {'Jméno': 'jmeno_osoba', 'Věk': 'vek_osoba', "Pes": "pes_majitel"}
list2 = []

for klic_slovnik in slovnik_header:
    # print("hledám pro:", klic_slovnik)
    for klic_data in list:
        if klic_slovnik == klic_data:
            # print("ANO", klic_data)
            value_slovnik = slovnik.get(klic_slovnik)
            list = [value_data.replace(klic_data, value_slovnik) for value_data in list]
            print(list)
        else:
            # print("nenalezena shoda:", klic_data)
            pass

# print(header_output)
