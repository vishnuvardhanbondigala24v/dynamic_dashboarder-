import pandas as pd

def clean_data(df):
    # Strip whitespace from column names
    df.columns = df.columns.str.strip()

    # Drop completely empty rows
    df.dropna(how='all', inplace=True)

    # Convert date columns
    for col in df.columns:
        if "date" in col.lower():
            try:
                df[col] = pd.to_datetime(df[col])
            except Exception:
                pass

    return df

def fill_missing(df, method="mean"):
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        if method == "mean":
            df[col].fillna(df[col].mean(), inplace=True)
        elif method == "median":
            df[col].fillna(df[col].median(), inplace=True)
    return df
