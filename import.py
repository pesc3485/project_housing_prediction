import pandas as pd

df = pd.read_csv(
    'Data/city_market_tracker.tsv',
    sep='\t',
    engine='pyarrow',
    dtype_backend='pyarrow',
    na_values=["", "NA", "NaN", "null"]
)

# First Clean
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

if "name" in df:
    df["name"] = df["name"].str.strip()

if "event_time" in df:
    df["event_time"] = pd.to_datetime(df["event_time"], errors="coerce", utc=True)

# Compressing to parquet file
df.to_parquet("cleaned.parquet", index=False)