import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

def transform(data):
    logging.info("Transforming data")
    # Convert list of dicts to DataFrame
    df = pd.DataFrame(data)

    # Basic cleaning: drop duplicates
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    logging.info(f"Dropped {before - after} duplicate rows")

    # Example aggregation: count posts per userId
    agg = df.groupby('userId').size().reset_index(name='post_count')

    logging.info(f"Aggregated post counts for {len(agg)} users")

    return df, agg

if __name__ == "__main__":
    # For quick local test
    from extract import extract
    raw_data = extract()
    df_clean, agg = transform(raw_data)
    print(df_clean.head())
    print(agg.head())
