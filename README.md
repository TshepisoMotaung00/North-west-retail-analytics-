# North-West Retail Analytics - Mahikeng HQ
From Mahikeng to Klerksdorp - 10,000 transactions analyzed with Python + SQL

### Results 💰
- Total: R136,017,466
- Top: Klerksdorp R27.6M
- Mahikeng R27.4M (HQ)

### 🦠 Raw vs Clean (Chapter 1)
This is the REAL work:
- Raw: `retail_sales.db` / `sales_raw` had `Rustenburg / RUSTENBURG / mahikeng / MAHIKENG`
- SQL Proof: `SELECT DISTINCT branch FROM sales_raw` returned 6 (fake count)
- Fix: `UPPER(TRIM(branch))` + `REPLACE(unit_price, 'R','')` + handle `;` delimiter
- Clean: 4 real branches ✅ + validated with `Retail_Sales_Clean_Data.csv`

### 📊 Data Science Pipeline
1. Data Engineering - Generated 10k rows (dirty)
2. ETL - Loaded CSV with `sep=';'` + SQLite `Retail_Sales.db`
3. Cleaning - SQL Rules in DBeaver
4. Analysis - `GROUP BY Store, SUM(Sales)` - Klerksdorp top
5. Visualization - matplotlib chart per branch

### How to Run
```bash
python big_data.py
python big_kpi.py
