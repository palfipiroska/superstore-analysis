def clean_data(df):
    # ensure correct types
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

    # drop obvious bad rows (if any)
    df = df.dropna()

    return df
