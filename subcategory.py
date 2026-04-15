import pandas as pd

df = pd.read_csv("orders.csv")

print(
    df.groupby("Sub-Category")["Profit"]
    .sum()
    .sort_values()
)
top5 = df.groupby(
    "Sub-Category")["Profit"].sum().sort_values(ascending=False).head(5)
print(top5)

print("Top 5 contribution:", top5.sum() / df["Profit"].sum())

worst5 = df.groupby("Sub-Category")["Profit"].sum().sort_values().head(5)
print(worst5)

print("Loss impact:", worst5.sum())

print(
    df.groupby("Sub-Category")["Discount"]
    .mean()
    .sort_values(ascending=False))


print(df.groupby("Sub-Category")
      [["Discount", "Profit"]].mean().sort_values("Profit"))
