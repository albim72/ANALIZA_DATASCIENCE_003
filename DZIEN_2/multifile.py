import dask.dataframe as dd

df = dd.read_csv("folder/*.csv")  # Wczytuje wiele plików naraz
df = df.compute()  # Konwersja na pandas (opcjonalnie)


import pandas as pd
import glob
from multiprocessing import Pool

# Znalezienie wszystkich plików CSV
csv_files = glob.glob("folder/*.csv")

# Funkcja do wczytania pojedynczego pliku
def load_csv(file):
    return pd.read_csv(file)

# Równoległe wczytanie plików
with Pool() as pool:
    dataframes = pool.map(load_csv, csv_files)

# Połączenie danych
df = pd.concat(dataframes, ignore_index=True)



import ujson
import glob
from concurrent.futures import ProcessPoolExecutor

json_files = glob.glob("folder/*.json")

def load_json(file):
    with open(file, "r") as f:
        return ujson.load(f)

with ProcessPoolExecutor() as executor:
    data = list(executor.map(load_json, json_files))



from PIL import Image
import glob
from concurrent.futures import ThreadPoolExecutor

image_files = glob.glob("folder/*.jpg")

def load_image(file):
    return Image.open(file).convert("RGB")

with ThreadPoolExecutor() as executor:
    images = list(executor.map(load_image, image_files))

import glob

text_files = glob.glob("folder/*.txt")

def load_text(file):
    with open(file, "r", encoding="utf-8") as f:
        return f.read()

with ThreadPoolExecutor() as executor:
    texts = list(executor.map(load_text, text_files))




