CREATE TABLE product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    description VARCHAR,
    category VARCHAR
)

INSERT INTO product (name, description, category)
VALUES
   ('iPhone X', 'Iphone 10, 1GB RAM, 128GB disk memory', 'Apple'),
   ('iPhone 12', 'Iphone 12, 1GB RAM, 128GB disk memory', 'Apple'),
   ('iPhone 13', 'Iphone 13, 1.5GB RAM, 128GB disk memory', 'Apple'),
   ('iPhone 14', 'Iphone 14, 2GB RAM, 256GB disk memory', 'Apple'),
   ('Samsung Galaxy S3', 'Samsung Galaxy S3, 1GB RAM, 50GB disk memory', 'Samsung'),
   ('Samsung Galaxy S4', 'Samsung Galaxy S4, 1.6GB RAM, 50GB disk memory', 'Samsung'),
   ('Samsung Galaxy S5', 'Samsung Galaxy S5, 2GB RAM, 100GB disk memory', 'Samsung'),
   ('Xiaomi 12', 'Xiaomi 12, 1GB RAM, 50GB disk memory', 'Xiaomi'),
   ('Xiaomi 13', 'Xiaomi 13, 2GB RAM, 100GB disk memory', 'Xiaomi'),
   ('NoName', 'Just no-name phone', NULL);

SELECT * FROM product;

CREATE TABLE category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR
);

INSERT INTO category (name)
VALUES
    ('Apple'),
    ('Samsung'),
    ('Xiaomi');

ALTER TABLE product
ADD COLUMN category_id INTEGER;

-- Unsupported operation
--ALTER TABLE product
--ADD CONSTRAINT fk_product_category_id
--FOREIGN KEY (category_id)
--REFERENCES category(id);

SELECT * FROM category;

UPDATE product
SET category_id = 1
WHERE category = 'Apple';

UPDATE product
SET category_id = 2
WHERE category = 'Samsung';

UPDATE product
SET category_id = 3
WHERE category = 'Xiaomi';

SELECT * FROM product;

-- Should work, but it doesn't
-- https://www.sqlite.org/lang_altertable.html
--ALTER TABLE product
--DROP COLUMN category;





