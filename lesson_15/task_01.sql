-- Количество людей старше 116 лет.
SELECT COUNT(*)
FROM user
WHERE AGE > 116;


SELECT
    SUM(age),  -- Сумму возрастов.
    AVG(age),  -- Средний возраст.
    SUM(age) / CAST(COUNT(*) AS FLOAT),  -- * Средний возраст, не используя функцию AVG.
    MIN(age),  -- Минимальный возраст.
    MAX(age),  -- Максимальный возраст.
    MAX(age) - MIN(age)  -- Разницу (в годах) между самым старшим и самым младшим человеком.
FROM user;
