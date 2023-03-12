-- Сгруппируйте данные в таблице user и посчитайте следующие статистики:

-- Количество людей из каждой страны.
SELECT country, COUNT(*)
FROM user
GROUP BY country
ORDER BY COUNT(*) DESC;

-- Количество людей для каждого имени (группировка по first_name).
SELECT first_name, COUNT(*) AS cnt
FROM user
GROUP BY first_name
ORDER BY cnt DESC;

-- Суммарное количество лет у людей из каждой страны.
SELECT country, SUM(age) AS sum_age
FROM user
GROUP BY country
ORDER BY sum_age DESC;

-- Среднее количество лет у людей из каждой страны.
SELECT country, AVG(age) AS average_age
FROM user
GROUP BY country
ORDER BY average_age DESC;

-- Возраст самого старшего человека из каждой страны.
SELECT country, MAX(age) AS max_age
FROM user
GROUP BY country
ORDER BY max_age DESC;

-- * Количество людей из каждой страны, у которой минимум 5 человек в таблице (используйте HAVING).
SELECT country, COUNT(*) AS cnt
FROM user
GROUP BY country
HAVING cnt >= 5
ORDER BY cnt DESC;

--  * Найдите количество людей с одинаковыми фамилиями.
SELECT last_name, COUNT(*) AS cnt
FROM user
GROUP BY last_name
HAVING cnt > 1;
