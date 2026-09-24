import sqlite3
conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

with open("analysis.sql","r") as f:
    queries = f.read().split(";")
    for q in queries:
        if q.strip():
            print("\n--- RESULT ---")
            print(q)
            cursor.execute(q)
            for row in cursor.fetchall()[:5]:
                print(row)

conn.close()