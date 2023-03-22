CREATE TABLE article (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR,
    "text" VARCHAR,
    author VARCHAR
);

INSERT INTO article (title, text, author)
VALUES
    ('Article 1', 'Long text of Article 1', 'Judy Hops'),
    ('Article 2', 'Long text of Article 2', 'John Doe'),
    ('Article 3', 'Long text of Article 3', 'Bill Jakobs');

SELECT * FROM article;

ALTER TABLE article
ADD COLUMN like_count integer;

SELECT * FROM article;

UPDATE article
SET like_count = 0;

SELECT * FROM article;

commit;