-- Отсортируйте данные в таблице user по:

-- Возрасту в обратном порядке
SELECT *
FROM user
ORDER BY age DESC;

-- По фамилии и имени.
SELECT *
FROM user
ORDER BY last_name, first_name;

-- По стране (в прямом порядке) и по возрасту (в обратном порядке).
SELECT *
FROM user
ORDER BY country, age DESC;

-- По длине полного имени (то есть по количеству символов имени + фамилии).
SELECT *
FROM user
ORDER BY LENGTH(first_name) + LENGTH(last_name);

-- По инициалам.
SELECT *
FROM user
ORDER BY SUBSTR(first_name, 1, 1), SUBSTR(last_name, 1, 1);