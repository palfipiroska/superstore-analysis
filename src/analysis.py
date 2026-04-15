import pandas as pd
import matplotlib.pyplot as plt


# -----------------------------
# 1. LOAD
# -----------------------------
def load_data(path="data/superstore.csv"):
    df = pd.read_csv(path)
    return df


# -----------------------------
# 2. BASIC CLEANING
# -----------------------------
def clean_data(df):
    # ensure correct types
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")
    df["Profit Margin"] = df["Profit"] / df["Sales"]

    # drop obvious bad rows (if any)
    df = df.dropna()

    return df


# -----------------------------
# 3. CORE ANALYSIS
# -----------------------------
def category_profit_analysis(df):
    return df.groupby("Sub-Category")["Profit"].sum().sort_values()


def category_discount_analysis(df):
    return df.groupby("Sub-Category")["Discount"].mean().sort_values(ascending=False)


def category_sales_analysis(df):
    return df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False)


def category_profit_margin_analysis(df):
    df["Profit Margin"] = df["Profit"] / df["Sales"]
    return df.groupby("Sub-Category")["Profit Margin"].mean().sort_values()


# -----------------------------
# 4. RUN PIPELINE
# -----------------------------
def create_charts(df):
    # -----------------------------
    # Chart 1: Profit by Sub-Category
    # -----------------------------
    profit_by_cat = df.groupby("Sub-Category")["Profit"].sum().sort_values()

    plt.figure()
    profit_by_cat.plot(kind="bar")
    plt.title("Profit by Sub-Category")
    plt.ylabel("Total Profit")
    plt.tight_layout()
    plt.show()

    # -----------------------------
    # Chart 2: Profit Margin vs Discount (relationship view)
    # -----------------------------

    summary = df.groupby("Sub-Category")[["Profit Margin", "Discount"]].mean()

    plt.figure()
    plt.scatter(summary["Discount"], summary["Profit Margin"])

    for i in summary.index:
        plt.text(summary.loc[i, "Discount"],
                 summary.loc[i, "Profit Margin"], i, fontsize=8)

    plt.title("Discount vs Profit Margin by Sub-Category")
    plt.xlabel("Average Discount")
    plt.ylabel("Average Profit Margin")
    plt.tight_layout()
    plt.show()


def main():
    df = load_data()
    df = clean_data(df)

    print("\nTOP LOSING CATEGORIES:")
    print(category_profit_analysis(df))

    print("\nHIGHEST DISCOUNT CATEGORIES:")
    print(category_discount_analysis(df))

    print("\nTOP SALES CATEGORIES:")
    print(category_sales_analysis(df))

    print("\nPROFIT MARGIN BY CATEGORY:")
    print(category_profit_margin_analysis(df))

    create_charts(df)


if __name__ == "__main__":
    main()
