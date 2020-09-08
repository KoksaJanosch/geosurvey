# excel to csv convertor:
import pandas as pd
import os
from pathlib import Path

# cesta k souborům
data_folder = Path("data/")

file = "DUN"    #####
xlsx = ".xlsx"
f_file = file + xlsx
ff = f_file

out = os.path.splitext(file)[0] + "_CSV_.csv"

read_file = pd.read_excel ( data_folder / ff)
read_file.to_csv (data_folder / out , index = None, header=True, sep=";")


