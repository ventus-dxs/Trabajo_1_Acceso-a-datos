import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "bar_local.db"

def get_conn():
    return sqlite3.connect(DB_PATH)

def crear_producto(producto):
    sql = """INSERT INTO productos (codigo,nombre,categoria,unidad,stock_actual,stock_minimo,precio_unit)
             VALUES (?, ?, ?, ?, ?, ?, ?)"""
    with get_conn() as conn:
        cur = conn.execute(sql, (producto['codigo'], producto['nombre'], producto.get('categoria'),
                                 producto.get('unidad'), producto.get('stock_actual',0),
                                 producto.get('stock_minimo',0), producto.get('precio_unit',0)))
        return cur.lastrowid

def leer_producto_por_codigo(codigo):
    with get_conn() as conn:
        cur = conn.execute("SELECT * FROM productos WHERE codigo = ?", (codigo,))
        row = cur.fetchone()
        if row:
            cols = [c[0] for c in cur.description]
            return dict(zip(cols, row))
        return None

def actualizar_stock(producto_id, delta):
    with get_conn() as conn:
        conn.execute("UPDATE productos SET stock_actual = stock_actual + ?, fecha_ultimo_mov = CURRENT_TIMESTAMP WHERE id = ?",
                     (delta, producto_id))
        conn.commit()

def eliminar_producto(producto_id):
    with get_conn() as conn:
        conn.execute("DELETE FROM productos WHERE id = ?", (producto_id,))
        conn.commit()
