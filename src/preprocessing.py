# preprocessing.py

import pandas as pd
from sklearn.preprocessing import StandardScaler


def clean_data(df):
    df = df.copy()
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df.dropna(inplace=True)
    return df


def encode_features(df, target_col, id_col=None):
    df = df.copy()

    if id_col and id_col in df.columns:
        df.drop(id_col, axis=1, inplace=True)

    X = df.drop(target_col, axis=1)
    y = df[target_col]

    X = pd.get_dummies(X, drop_first=True)
    return X, y


def scale_features(X_train, X_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled