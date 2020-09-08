# import pandas as pd
# from pathlib import Path

# # cesta k souborům
# data_folder = Path("data/")
#
#
# read_file = pd.read_csv ( data_folder / "DUN_completed.csv", sep=";")
# read_file.to_excel ( data_folder / "DUN_final.xlsx", index = None, header=True)
#
#
#

# csv to excel convertor:
import os
import pandas as pd
from pathlib import Path

# cesta k souborům
data_folder = Path("data/")

file = "v"    #####
csv = "_CSV__completed.csv"
f_file = file + csv
ff = f_file

out = os.path.splitext(file)[0] + "_final.xlsx"



read_file = pd.read_csv ( data_folder / ff, sep=";")
read_file.to_excel ( data_folder / out, index = None, header=True)
