# E-commerce API Pipeline - Medallion Architecture

End-to-end Data Engineering project ingesting live product data from DummyJSON API.

## 🏗️ Medallion Architecture
 Bronze -> Silver -> Gold

- **Bronze (Raw):** bronze/raw_products.json
- **Silver (Cleaned):** silver/cleaned_products.csv  
- **Gold (Analytics):** ecommerce.db

## 🛠️ Tech Stack
Python, Pandas, Requests, SQLite

## 🚀 How to run
pip install requests pandas

python API_project.py

python run_sql.py

## 📊 Output - Gold Layer Analytics

OUTPUT:

Pipeline Run:
Fetching from API... 
Bronze: 100 products
Gold: Loaded to ecommerce.db
Success! Exit code 0

Category Performance:
- mens-watches: 6 products, Avg $8098
- laptops: 5 products, Avg $1559
- furniture: 5 products, Avg $1199

Top Products:
- Rolex Cellini: $8999, Rating 4.97
- Colombo Bed: $1899, Rating 4.77

Insight: Mens-watches is highest value.
