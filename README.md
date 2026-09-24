# E-commerce Data Engineering Project - API to Gold

### Medallion Architecture: Bronze -> Silver -> Gold

**Tech Stack:** Python, Requests API, Pandas, SQLite, SQL

**What I did:**
1.  **Bronze:** Fetched 100 live products from DummyJSON API and saved as raw JSON
2.  **Silver:** Cleaned with Pandas (deduplication, null handling, type conversion)
3.  **Gold:** Loaded into SQLite `ecommerce.db` -> table `api_products`

**Business Analysis (SQL):**
- Category-wise avg price & stock analysis
- Top rated high-value products for marketing focus

How to run:
```bash
pip install requests pandas
python API_project.py
python run_sql.py
```
## 📊 Output - Gold Layer Analytics

**Pipeline Run:**
Fetching from API...
Bronze: 100 products
Gold: Loaded to ecommerce.db -> table api_products
Process finished with exit code 0

**Query 1: Category Performance**
('mens-watches', 6, 8098.32, 349)
('laptops', 5, 1559.99, 258)
('furniture', 5, 1199.99, 245)

Insight: Mens-watches is highest value category.

**Query 2: Top Rated Premium Products**
('Rolex Cellini Date Black Dial', 'Rolex', 8999.99, 4.97, 40)
('Annibale Colombo Bed', 'Annibale Colombo', 1899.99, 4.77, 88)

Insight: Rolex has highest price with near-perfect rating.
