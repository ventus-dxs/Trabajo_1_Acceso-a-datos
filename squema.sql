-- src/db/schema.sql

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS productos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  codigo TEXT UNIQUE NOT NULL,
  nombre TEXT NOT NULL,
  categoria TEXT,
  unidad TEXT,          -- ej. 'botella', 'litro', 'kilo'
  stock_actual REAL NOT NULL DEFAULT 0,
  stock_minimo REAL NOT NULL DEFAULT 0,
  precio_unit REAL NOT NULL DEFAULT 0,
  fecha_ultimo_mov DATETIME
);

CREATE TABLE IF NOT EXISTS movimientos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  producto_id INTEGER NOT NULL,
  tipo TEXT CHECK(tipo IN ('entrada','salida','ajuste')) NOT NULL,
  cantidad REAL NOT NULL,
  fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
  nota TEXT,
  FOREIGN KEY(producto_id) REFERENCES productos(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_producto_codigo ON productos(codigo);
CREATE INDEX IF NOT EXISTS idx_mov_producto ON movimientos(producto_id);
