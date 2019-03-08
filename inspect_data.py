import pandas as pd

data = pd.read_excel("BCN_trimestral_2018.xlsx")

#argumentos del read excel.

print(data.dtypes)

print(data["Compravendes d'habitatge registrades a Barcelona"])

print(data)