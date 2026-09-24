import requests
import pandas as pd
import sqlite3
import json
from datetime import datetime

print("Fetching from API...")
url = "https://dummyjson.com/products?limit=100"
response = requests.get(url)
data = response.json()

with open("bronze_api_raw.json", "w") as f:
    json.dump(data, f, indent=2)

df = pd.DataFrame(data['products'])
print(f"Bronze: {len(df)} products")

df_clean = df[['id', 'title', 'price', 'category', 'stock', 'rating', 'brand']].copy()
df_clean = df_clean.drop_duplicates(subset=['id'])
df_clean['price'] = pd.to_numeric(df_clean['price'], errors='coerce')
df_clean = df_clean.dropna(subset=['price', 'title'])
df_clean['fetch_date'] = datetime.now()

conn = sqlite3.connect("ecommerce.db")
df_clean.to_sql("api_products", conn, if_exists="replace", index=False)
conn.close()

print("Gold: Loaded to ecommerce.db -> table api_products ✅")