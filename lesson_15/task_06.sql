-- Создайте таблицы Product и Vendor, заполните их данными (просто скопируйте запросы из комментария к слайду).
CREATE TABLE vendor (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   name VARCHAR UNIQUE NOT NULL
);

CREATE TABLE product (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   name VARCHAR UNIQUE NOT NULL,
   price FLOAT NOT NULL,
   vendor_id INTEGER NOT NULL,
   FOREIGN KEY(vendor_id) REFERENCES vendor(id)
);

INSERT INTO vendor (id, name)
VALUES
   (1, 'Apple'),
   (2, 'Samsung'),
   (3, 'Xiaomi'),
   (4, 'Nokia');

INSERT INTO product (name, price, vendor_id)
VALUES
   ('iPhone X', 1000, 1),
   ('iPhone 12', 1200, 1),
   ('iPhone 13', 1300, 1),
   ('iPhone 14', 1400, 1),
   ('Samsung Galaxy S3', 800, 2),
   ('Samsung Galaxy S4', 900, 2),
   ('Samsung Galaxy S5', 1000, 2),
   ('Xiaomi 12', 600, 3),
   ('Xiaomi 13', 700, 3),
   ('NoName', 100, -1);


-- Сделайте JOIN запрос для данных из таблиц Product и Vendor, посмотрите на результат. Какие названия столбцов получились в результате?
SELECT *
FROM product
JOIN vendor ON product.vendor_id = vendor.id;

-- Сделайте разные типы JOIN запросов (INNER, LEFT OUTER, RIGHT OUTER, FULL OUTER). Как отличаются результаты?
SELECT *
FROM product
JOIN
-- INNER JOIN
-- LEFT OUTER JOIN
-- RIGHT OUTER JOIN
-- FULL OUTER JOIN
vendor ON product.vendor_id = vendor.id;

-- * Сделайте запрос, который выведет сколько продуктов у каждого вендора (используйте JOIN и GROUP BY).
SELECT vendor.name, COUNT(*)
FROM vendor
LEFT JOIN product ON vendor.id = product.vendor_id
GROUP BY vendor.name;

-- * Сделайте запрос, который выведет среднюю цену продуктов у каждого вендора
SELECT vendor.name, AVG(product.price)
FROM vendor
LEFT JOIN product ON vendor.id = product.vendor_id
GROUP BY vendor.name;

-- ** Сделайте запрос, который выведет вендоров, у которых нет продуктов (используйте JOIN, GROUP BY, HAVING).
SELECT vendor.name
FROM vendor
LEFT JOIN product ON vendor.id = product.vendor_id
GROUP BY vendor.name
HAVING COUNT(product.id) = 0;
