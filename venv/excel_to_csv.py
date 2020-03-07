# excel to csv convertor:
import pandas as pd
from pathlib import Path

# cesta k souborům
data_folder = Path("data/")

read_file = pd.read_excel ( data_folder / r"test_1.xlsx")
read_file.to_csv (data_folder / r"vzor.csv", index = None, header=True, sep=";")