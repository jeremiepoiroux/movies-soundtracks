import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging

# Configure logging
logging.basicConfig(filename='scraping.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Accept-Language": "en-US,en;q=0.5"
}

def get_soundtrack(soundtrack_url):
    concatenated_info = []
    try:
        with requests.Session() as session:
            response = session.get(soundtrack_url, headers=headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
            soup = BeautifulSoup(response.text, 'html.parser')
            spans = soup.find_all("span", class_="ipc-metadata-list-item__label")

            for span in spans:
                span_text = span.text.strip()
                link = span.find_next("div", class_="ipc-html-content-inner-div")
                if link:
                    link_text = link.text.strip()
                    concatenated_info.append(span_text + ", " + link_text)

            concatenated_string = " | ".join(concatenated_info)
            return concatenated_string
    except Exception as e:
        logging.error(f"Error fetching soundtrack from {soundtrack_url}: {e}")
        return None

def process_row(index, row):
    soundtrack_url = row["Soundtrack_URL"]
    title = row["Title"]

    if title:
        try:
            # Delay to avoid hitting rate limits
            time.sleep(0.5)
            soundtrack = get_soundtrack(soundtrack_url)
            return index, soundtrack
        except Exception as e:
            logging.error(f"Error processing row {index}: {e}")
            return index, None
    else:
        return index, None

def main(start_index, end_index):
    # Load the data
    data_csv = pd.read_csv('updated_URLlist_large_master.csv')

    # Extract the subset of rows to process (inclusive of start_index and end_index)
    indices_to_scrape = range(start_index, end_index + 1)
    data_subset = data_csv.loc[indices_to_scrape].reset_index(drop=True)

    # Initialize ThreadPoolExecutor for parallel processing
    total_rows = len(data_subset)
    batch_size = 1000
    batch_count = 0

    # Prepare the progress bar
    with tqdm(total=total_rows, desc="Processing rows", initial=0) as pbar:
        with ThreadPoolExecutor(max_workers=5) as executor:  # Reduce max_workers to be less aggressive
            futures = {executor.submit(process_row, i, data_subset.loc[i]): i for i in range(total_rows)}

            for future in as_completed(futures):
                index, soundtrack = future.result()
                original_index = indices_to_scrape[index]  # Map back to original index
                data_csv.loc[original_index, "Soundtrack"] = soundtrack

                # Update CSV every X rows
                if (index + 1) % batch_size == 0:
                    batch_count += 1
                    data_csv.iloc[:(original_index + 1)].to_csv(f'updated_data_batch_{batch_count}.csv', index=False)
                    print(f"Batch {batch_count} saved to 'updated_data_batch_{batch_count}.csv'")

                # Update the progress bar
                pbar.update(1)

    # Save the final modified DataFrame back to CSV
    data_csv.to_csv('updated_data.csv', index=False)
    print("Processing completed and data saved to 'updated_data.csv'")

# Example usage: specify start_index and end_index
start_index = 0
end_index = 10000
main(start_index, end_index)
