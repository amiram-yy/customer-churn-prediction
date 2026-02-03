# features.py

def add_custom_features(df):
    df = df.copy()

    df["tenure_group"] = pd.cut(
        df["tenure"],
        bins=[0, 12, 24, 48, 72],
        labels=["0-1y", "1-2y", "2-4y", "4-6y"]
    )

    return df