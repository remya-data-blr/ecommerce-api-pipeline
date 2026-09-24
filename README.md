# E-commerce API Pipeline

Live API -> Bronze -> Silver -> Gold

Tech: Python, Pandas, SQLite
API: dummyjson.com/products

How to run:
1. pip install requests pandas
2. python API_project.py
3. python run_sql.py

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
