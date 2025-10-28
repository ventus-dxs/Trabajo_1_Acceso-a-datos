import sqlite3

PRAGMA foreign_keys = ON;

-- =======================
-- TABLA: productos
-- =======================
INSERT INTO productos (codigo, nombre, categoria, unidad, stock_actual, stock_minimo, precio_unit, fecha_ultimo_mov)
VALUES
-- BEBIDAS
('BEB-001', 'Coca-Cola 2L', 'Bebidas', 'botella', 25, 5, 1.50, CURRENT_TIMESTAMP),
('BEB-002', 'Coca-Cola Zero 2L', 'Bebidas', 'botella', 18, 5, 1.60, CURRENT_TIMESTAMP),
('BEB-003', 'Agua mineral 0.5L', 'Bebidas', 'botella', 50, 10, 0.80, CURRENT_TIMESTAMP),
('BEB-004', 'Fanta Naranja 1.5L', 'Bebidas', 'botella', 20, 5, 1.40, CURRENT_TIMESTAMP),
('BEB-005', 'Cerveza Mahou 33cl', 'Bebidas', 'botella', 60, 10, 1.20, CURRENT_TIMESTAMP),

-- LICORES
('LIC-001', 'Ron Barceló Añejo', 'Licores', 'botella', 12, 3, 13.50, CURRENT_TIMESTAMP),
('LIC-002', 'Whisky J&B', 'Licores', 'botella', 8, 2, 15.00, CURRENT_TIMESTAMP),
('LIC-003', 'Vodka Absolut', 'Licores', 'botella', 10, 3, 14.50, CURRENT_TIMESTAMP),
('LIC-004', 'Ginebra Beefeater', 'Licores', 'botella', 9, 2, 16.00, CURRENT_TIMESTAMP),
('LIC-005', 'Tequila José Cuervo', 'Licores', 'botella', 7, 2, 17.50, CURRENT_TIMESTAMP),

-- CAFÉS
('CAF-001', 'Café Espresso', 'Café', 'vaso', 100, 20, 1.00, CURRENT_TIMESTAMP),
('CAF-002', 'Café con leche', 'Café', 'vaso', 90, 20, 1.20, CURRENT_TIMESTAMP),
('CAF-003', 'Café cortado', 'Café', 'vaso', 85, 20, 1.10, CURRENT_TIMESTAMP),
('CAF-004', 'Capuccino', 'Café', 'vaso', 40, 10, 1.50, CURRENT_TIMESTAMP),
('CAF-005', 'Café descafeinado', 'Café', 'vaso', 50, 10, 1.10, CURRENT_TIMESTAMP),

-- SNACKS
('SNK-001', 'Patatas fritas', 'Snacks', 'bolsa', 40, 10, 0.90, CURRENT_TIMESTAMP),
('SNK-002', 'Frutos secos mixtos', 'Snacks', 'bolsa', 35, 10, 1.20, CURRENT_TIMESTAMP),
('SNK-003', 'Aceitunas rellenas', 'Snacks', 'tarro', 25, 5, 1.80, CURRENT_TIMESTAMP),
('SNK-004', 'Nachos con queso', 'Snacks', 'ración', 20, 5, 3.50, CURRENT_TIMESTAMP),
('SNK-005', 'Mini croquetas', 'Snacks', 'ración', 15, 5, 4.00, CURRENT_TIMESTAMP);

-- =======================
-- TABLA: movimientos
-- =======================
INSERT INTO movimientos (producto_id, tipo, cantidad, fecha, nota)
VALUES
-- Entradas de stock (compras a proveedores)
(1, 'entrada', 30, '2025-10-20 10:00:00', 'Reposición Coca-Cola'),
(2, 'entrada', 25, '2025-10-20 10:10:00', 'Reposición Coca-Cola Zero'),
(3, 'entrada', 60, '2025-10-21 09:30:00', 'Compra de agua mineral'),
(4, 'entrada', 20, '2025-10-21 09:45:00', 'Reposición de Fanta'),
(5, 'entrada', 80, '2025-10-21 10:00:00', 'Cerveza Mahou'),

-- Ventas (salidas)
(1, 'salida', 5, '2025-10-22 18:30:00', 'Venta a clientes'),
(2, 'salida', 8, '2025-10-22 19:00:00', 'Venta a clientes'),
(5, 'salida', 12, '2025-10-22 22:00:00', 'Consumo en barra'),

-- Ajustes (por roturas o caducidad)
(3, 'ajuste', -2, '2025-10-23 12:00:00', 'Botellas dañadas'),
(4, 'ajuste', -1, '2025-10-23 12:15:00', 'Producto caducado'),

-- Movimientos de licores
(6, 'entrada', 10, '2025-10-19 11:00:00', 'Compra a distribuidor'),
(7, 'entrada', 8, '2025-10-19 11:15:00', 'Compra a distribuidor'),
(6, 'salida', 3, '2025-10-24 22:00:00', 'Venta de copas'),
(7, 'salida', 2, '2025-10-24 22:10:00', 'Venta de copas'),

-- Movimientos de café
(11, 'entrada', 200, '2025-10-18 08:00:00', 'Entrega semanal de café'),
(11, 'salida', 50, '2025-10-24 10:00:00', 'Ventas de cafés'),
(12, 'salida', 45, '2025-10-24 10:10:00', 'Ventas de cafés con leche'),
(13, 'salida', 30, '2025-10-24 10:15:00', 'Ventas de cortados'),

-- Movimientos de snacks
(16, 'entrada', 50, '2025-10-18 09:00:00', 'Compra a proveedor'),
(17, 'entrada', 50, '2025-10-18 09:05:00', 'Compra a proveedor'),
(18, 'salida', 5, '2025-10-23 20:30:00', 'Venta de aceitunas'),
(19, 'salida', 4, '2025-10-23 21:00:00', 'Venta de nachos'),
(20, 'salida', 3, '2025-10-23 21:15:00', 'Venta de croquetas');
