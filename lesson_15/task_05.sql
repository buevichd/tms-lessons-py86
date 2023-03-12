-- Напишите запрос, который находит страну самого старшего человека.
SELECT country
FROM user
WHERE age = (SELECT MAX(age) FROM user)
LIMIT 1;

-- Используя прошлое задание как подзапрос, напишите запрос который находит всех людей из той же страны, из которой самый старший человек.
SELECT *
FROM user
WHERE country = (
    SELECT country
    FROM user
    WHERE age = (SELECT MAX(age) FROM user)
    LIMIT 1
);

-- * Выведите информацию обо всех людях, у которых есть однофамильцы в таблице.
SELECT *
FROM user
WHERE last_name IN (
    SELECT last_name
    FROM user
    GROUP BY last_name
    HAVING COUNT(*) > 1
)
ORDER BY last_name;
