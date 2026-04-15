import pandas as pd
import matplotlib.pyplot as plt
import os


# -----------------------------
# 1. LOAD DATA
# -----------------------------
def load_data(path="data/superstore.csv"):
    return pd.read_csv(path)


# -----------------------------
# 2. CLEANING
# -----------------------------
def clean_data(df):
    df = df.copy()

    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

    # remove broken rows
    df = df.dropna()

    # avoid divide-by-zero issues
    df = df[df["Sales"] != 0]

    return df


# -----------------------------
# 3. FEATURE ENGINEERING
# -----------------------------
def add_features(df):
    df = df.copy()

    df["Profit Margin"] = df["Profit"] / df["Sales"]

    return df


# -----------------------------
# 4. ANALYSIS TABLES
# -----------------------------
def category_summary(df):
    summary = df.groupby("Sub-Category").agg(
        sales=("Sales", "sum"),
        profit=("Profit", "sum"),
        discount=("Discount", "mean"),
        margin=("Profit Margin", "mean")
    )

    summary["efficiency"] = summary["profit"] / summary["sales"]

    return summary.sort_values("efficiency")


def profitability_ranking(df):
    return df.groupby("Sub-Category")["Profit"].sum().sort_values()


def sales_ranking(df):
    return df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False)


# -----------------------------
# 5. VISUALS
# -----------------------------
def create_charts(df, output_dir="outputs/charts"):
    os.makedirs(output_dir, exist_ok=True)

    # -----------------------------
    # Chart 1: Profit by Sub-Category
    # -----------------------------
    profit = df.groupby("Sub-Category")["Profit"].sum().sort_values()

    plt.figure()
    profit.plot(kind="bar")
    plt.title("Profit by Sub-Category")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/profit_by_subcategory.png")
    plt.close()

    # -----------------------------
    # Chart 2: Danger Zone
    # Discount vs Profit Margin
    # -----------------------------
    summary = df.groupby("Sub-Category").agg(
        discount=("Discount", "mean"),
        margin=("Profit Margin", "mean")
    )

    plt.figure()
    plt.scatter(summary["discount"], summary["margin"])

    for name in summary.index:
        plt.text(
            summary.loc[name, "discount"],
            summary.loc[name, "margin"],
            name,
            fontsize=8
        )

    plt.title("Danger Zone: Discount vs Profit Margin")
    plt.xlabel("Average Discount")
    plt.ylabel("Average Profit Margin")

    plt.tight_layout()
    plt.savefig(f"{output_dir}/danger_zone.png")
    plt.close()


# -----------------------------
# 6. PIPELINE
# -----------------------------
def main():
    df = load_data()
    df = clean_data(df)
    df = add_features(df)

    print("\n=== CATEGORY SUMMARY (Efficiency Ranking) ===")
    print(category_summary(df))

    print("\n=== MOST UNPROFITABLE CATEGORIES ===")
    print(profitability_ranking(df))

    print("\n=== TOP SALES CATEGORIES ===")
    print(sales_ranking(df))

    create_charts(df)

    print("\nCharts saved to outputs/charts/")


if __name__ == "__main__":
    main()
