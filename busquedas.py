import sqlite3
from pathlib import Path

SELECT * FROM productos WHERE nombre LIKE '%Coca%';



SELECT id, nombre, stock_actual FROM productos ORDER BY stock_actual ASC;


SELECT categoria, COUNT(*) AS total_prod, SUM(stock_actual) AS stock_total
FROM productos
GROUP BY categoria
ORDER BY stock_total DESC;



SELECT p.id, p.nombre, m.tipo, m.cantidad, m.fecha
FROM productos p
LEFT JOIN movimientos m ON m.producto_id = p.id
WHERE m.id = (
  SELECT id FROM movimientos WHERE producto_id = p.id ORDER BY fecha DESC LIMIT 1
);



SELECT id, nombre, stock_actual, stock_minimo FROM productos WHERE stock_actual < stock_minimo;
