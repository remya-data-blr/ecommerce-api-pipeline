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

**How to run:**

1.pip install requests pandas 

2.python API_project.py 

3.python run_sql.py
