from dataclasses import dataclass

from flask import Flask, abort, redirect, session, request
from flask_session import Session
import sqlite3

DATABASE_FILE = 'db.sqlite3'

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@dataclass
class Article:
    id: int
    title: str
    text: str
    author: str
    like_count: int


def get_all_articles() -> list[Article]:
    with sqlite3.connect(DATABASE_FILE) as connection:
        execution_result = connection.execute(
            'SELECT id, title, text, author, like_count FROM article')
        return [Article(*values) for values in execution_result.fetchall()]


def get_article(article_id: int) -> Article:
    with sqlite3.connect(DATABASE_FILE) as connection:
        execution_result = connection.execute('SELECT id, title, text, author, like_count '
                                              'FROM article '
                                              'WHERE id = ?', (article_id,))
        rows = execution_result.fetchall()
        if len(rows) != 1:
            raise ValueError(f'Expected 1 object with id {article_id}, got {len(rows)}')
        return Article(*rows[0])


def save_article(article: Article):
    with sqlite3.connect(DATABASE_FILE) as connection:
        data = (article.title, article.text, article.author, article.like_count, article.id)
        connection.execute('UPDATE article '
                           'SET title = ?, text = ?, author = ?, like_count = ? '
                           'WHERE id = ?', data)


@app.route('/')
@app.route('/articles')
def articles_view():
    articles = get_all_articles()
    articles_html = '\n'.join(
        f'<li><a href="/article/{article.id}">{article.title}</a></li>'
        for article in articles)

    return f'''
    <html>
        <head>
            <title>Articles APP</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.4.1/dist/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
        </head>
        <body>
            <h1>All Articles</h1>
            <ul>
                {articles_html}
            </ul>
        </body>
    </html>
    '''


@app.route('/article/<int:article_id>')
def article_view(article_id: int):
    try:
        article = get_article(article_id)
    except ValueError as e:
        abort(404, e)

    return f'''
    <html>
        <head>
            <title>Articles APP</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.4.1/dist/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
        </head>
        <body>
            <a href="/articles">Main page</a>
            <h1>{article.title}</h1>
            <h3>Author: {article.author}</h3>
            <p>{article.text}</p>
            <p>Like count: {article.like_count}</p>
            <form method="post" action="/article/like">
                <input type="hidden" name="article_id" value="{article.id}"/>
                <input type="submit" value="Like"/>
            </form>
        </body>
    </html>
    '''


@app.route('/article/like', methods=['POST'])
def like_article():
    article_id = int(request.form['article_id'])
    article = get_article(article_id)
    liked_articles = session.setdefault('liked_articles', set())
    if article.id in liked_articles:
        article.like_count -= 1
        liked_articles.remove(article.id)
    else:
        article.like_count += 1
        liked_articles.add(article.id)
    save_article(article)
    return redirect(f'/article/{article.id}')


if __name__ == '__main__':
    app.run(port=8081, debug=True)
