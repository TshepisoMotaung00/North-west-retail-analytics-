import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "big_retail_sales.csv",
    sep=";"
)

total = df["Sales"].sum()

by_store = df.groupby(
    "Store"
)["Sales"].sum().sort_values(
    ascending=False
)

print(f"Total Revenue: R{total:,.0f}")
print(by_store)
print(f"Top: {by_store.index[0]}")

plt.figure(figsize=(8,5))
by_store.plot(
    kind="bar",
    color=["#003366","#0066CC","#3399FF","#66B2FF","#99CCFF"]
)
plt.title(
    "North West - Sales by Store"
)
plt.ylabel("Sales (R)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("big_kpi.png")
print("Chart saved!")
