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
pip install requests pandas

python API_project.py

python run_sql.py
