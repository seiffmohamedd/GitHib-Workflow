import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

API_URL = "https://jsonplaceholder.typicode.com/posts"

def extract():
    logging.info(f"Extracting data from {API_URL}")
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Will raise HTTPError if status is not 200
        data = response.json()
        logging.info(f"Extracted {len(data)} records")
        return data
    except requests.RequestException as e:
        logging.error(f"Failed to extract data: {e}")
        raise

if __name__ == "__main__":
    extract()
