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

Pipeline Run:
Fetching from API...
Bronze: 100 products saved
Gold: Loaded to ecommerce.db -> table api_products
Process finished with exit code 0

Query 1: Category Performance
mens-watches | 6 products | Avg $8098.32 | Stock 349
laptops | 5 products | Avg $1559.99 | Stock 258
furniture | 5 products | Avg $1199.99 | Stock 245

Insight: Mens-watches is highest value category.

Query 2: Top Rated Premium Products
Rolex Cellini - $8999.99 - Rating 4.97
Annibale Colombo Bed - $1899.99 - Rating 4.77
Huawei Matebook X Pro - $1399.99 - Rating 4.98

Insight: Rolex has highest price with near-perfect rating.
