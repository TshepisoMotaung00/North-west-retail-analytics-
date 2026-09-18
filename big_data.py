import pandas as pd
import random
from datetime import datetime, timedelta

stores = [
    "Mahikeng",
    "Klerksdorp",
    "Potchefstroom",
    "Zeerust",
    "Lichtenburg"
]

rows = []
start = datetime(2024, 1, 1)

for i in range(10000):
    date = (
        start + timedelta(days=random.randint(0, 364))
    ).strftime("%Y-%m-%d")
    store = random.choice(stores)
    sales = random.randint(5, 3000)
    rows.append([date, store, sales])

df = pd.DataFrame(
    rows,
    columns=["Date", "Store", "Sales"]
)

df.to_csv(
    "big_retail_sales.csv",
    index=False,
    sep=";"
)

print("BIG DATA CREATED for North West: 10000 rows!")
