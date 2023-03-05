-- Найдите людей из Японии в таблице.
SELECT *
FROM user
WHERE country = 'Япония';

-- Сколько людей из Японии в таблице?
-- Используйте COUNT(*)
SELECT COUNT(*)
FROM user
WHERE country = 'Япония';

-- Найдите всех людей с именем Мария.
SELECT *
FROM user
WHERE first_name = 'Мария';

-- Найдите людей старше 116 лет.
SELECT *
FROM user
WHERE age > 116;

-- Выведите людей в порядке возрастания возраста.
-- Используйте ORDER BY.
SELECT *
FROM user
ORDER BY age;

-- Кто самый старейший человек в таблице?
-- Используйте ORDER BY ... DESC + LIMIT 1.
SELECT *
FROM user
ORDER BY age DESC
LIMIT 1;

-- * Сколько людей из каждой страны в таблице?
-- Выведите страны в порядке убывания количества людей.
SELECT country, count(*) AS cnt
FROM user
GROUP BY country
ORDER BY cnt DESC;
