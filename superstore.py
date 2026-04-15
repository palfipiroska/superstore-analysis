import pandas as pd

df = pd.read_csv("orders.csv")

print(df.head())

print("TOTAL SALES:", df["Sales"].sum())
print("TOTAL PROFIT:", df["Profit"].sum())
print("AVERAGE DISCOUNT:", df["Discount"].mean())

print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))

loss_df = df[df["Profit"] < 0]
print(loss_df.groupby("Category")["Profit"].sum())

print(
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print(
    df.groupby("Product Name")["Profit"]
    .sum()
    .sort_values()
    .head(10)
)
df.groupby("Sub-Category")["Profit"].sum().sort_values()
df[df["Profit"] < 0].groupby("Product Name")[
    "Profit"].sum().sort_values().head(10)
df.groupby("Discount")["Profit"].mean()
