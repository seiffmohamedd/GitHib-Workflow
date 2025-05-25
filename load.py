import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

def load(clean_df, agg_df, clean_path='clean_data.csv', agg_path='agg_data.csv'):
    logging.info(f"Saving clean data to {clean_path}")
    clean_df.to_csv(clean_path, index=False)
    logging.info(f"Saving aggregated data to {agg_path}")
    agg_df.to_csv(agg_path, index=False)
    logging.info("Data loading complete")

if __name__ == "__main__":
    # For local quick test
    from extract import extract
    from transform import transform
    raw = extract()
    clean_df, agg_df = transform(raw)
    load(clean_df, agg_df)
