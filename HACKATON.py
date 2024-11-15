import csv
import pandas as pd

url_1 = "Sprints.csv" # Ему соответствует arr_s
url_2 = "History.csv" # Ему соответствует arr_h
url_3 = "Data.csv" # Ему соответствует arr_d


with open(url_1, encoding="utf-8") as f: arr_s = pd.DataFrame([i for i in csv.reader(f, delimiter=";")][2:])
with open(url_2, encoding="utf-8") as f: arr_h = pd.DataFrame([i for i in csv.reader(f, delimiter=";")][2:])
with open(url_3, encoding="utf-8") as f: arr_d = pd.DataFrame([i for i in csv.reader(f, delimiter=";")][2:])

print(arr_s)
print(arr_h)
print(arr_d)