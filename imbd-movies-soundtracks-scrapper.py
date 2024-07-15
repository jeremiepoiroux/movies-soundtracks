import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import json
from tqdm import tqdm

data_csv = pd.read_csv('data.csv')

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0", "Accept-Language": "en-US,en;q=0.5"}

def get_soundtrack(soundtrack_url):
    concatenated_info = []  # Initialize as an empty list
    concatenated_string = ()
    response = requests.get(soundtrack_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    spans = soup.find_all("span", class_="ipc-metadata-list-item__label")

    for span in spans:
        span_text = span.text.strip()
        link = span.find_next("div", class_="ipc-html-content-inner-div")
        if link:
            link_text = link.text.strip()
            concatenated_info.append(span_text + ", " + link_text)
            concatenated_string = ["', '".join(concatenated_info)]

    return concatenated_string

total_rows = len(data_csv)

# Initialize tqdm with total number of rows
for i in tqdm(range(total_rows)[0:1], desc="Processing rows", initial=0):
    soundtrack_url = data_csv.loc[i, "Soundtrack_URL"]
    title = data_csv.loc[i, "Title"]

    if title:
        try:
            time.sleep(0.5)  # Adding a delay before the request
            soundtrack = get_soundtrack(soundtrack_url)
            data_csv.loc[i, "Soundtrack"] = soundtrack
        except Exception as e:
            print(f"Error fetching soundtrack for row {i}: {e}")
            data_csv.loc[i, "Soundtrack"] = None
    else:
        # Skip the row if the title is empty
        data_csv.loc[i, "Soundtrack"] = None

# Save the modified DataFrame back to CSV
data_csv.to_csv('updated_data.csv', index=False)
print("Processing completed and data saved to 'updated_data.csv'")
