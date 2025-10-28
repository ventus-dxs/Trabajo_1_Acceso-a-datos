import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "bar_local.db"

def init_local_db():
    conn = sqlite3.connect(DB_PATH)
    try:
        with open(Path(__file__).parent / "schema.sql", "r", encoding="utf8") as f:
            conn.executescript(f.read())
        conn.commit()
    finally:
        conn.close()

def seed_data():
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute("INSERT OR IGNORE INTO productos (codigo,nombre,categoria,unidad,stock_actual,stock_minimo,precio_unit) VALUES (?,?,?,?,?,?,?)",
                    ("COKE-001","Coca-Cola 2L","Bebida","botella",10,2,1.5))
        conn.commit()
    finally:
        conn.close()
