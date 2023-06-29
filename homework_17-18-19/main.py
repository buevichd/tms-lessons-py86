import sqlite3
from dataclasses import dataclass
from flask import Flask, session, redirect
from flask_session import Session


DATABASE_FILE = 'db_4.sqlite3'

app = Flask(__name__)
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


@dataclass
class Product:
    id: int
    name: str
    description: str
    category: str


def load_products() -> list[Product]:
    with sqlite3.connect(DATABASE_FILE) as connection:
        rows = connection.execute('SELECT id, name, description, category FROM product')
        return [Product(*row) for row in rows]


def load_product(product_id: int) -> Product:
    with sqlite3.connect(DATABASE_FILE) as connection:
        rows = connection.execute(
            'SELECT id, name, description, category '
            'FROM product '
            'WHERE id = ?',
            [product_id]).fetchall()
        assert len(rows) == 1
        return Product(*rows[0])


@app.route('/products')
def products_view():
    products = load_products()
    products_html = ''
    for product in products:
        products_html += f'<li><a href="/product/{product.id}">{product.name}</a></li>'
    return f'''
    <html>
    <head>
        <title>Shop APP</title>
    </head>
    <body>
        <h1>Products</h1>
        <ul>
            {products_html}
        </ul>
    </body>
    </html>
    '''


@app.route('/product/<int:product_id>')
def product_view(product_id: int):
    product = load_product(product_id)
    favorite_product_ids = session.get('favorite_product_ids', set())

    product_title = product.name
    start_button_text = 'Add to favorites'
    if product_id in favorite_product_ids:
        product_title += ' &#10027;'
        start_button_text = 'Remove from favorites'

    return f'''
    <html>
    <head>
        <title>Shop APP</title>
    </head>
    <body>
        <a href="/products">Go to products page</a>
        <h1>{product_title}</h1>
        <h2>{product.category}</h2>
        <p>{product.description}</p>
        <form method="post" action="/product/{product.id}/star">
            <input type="submit" value="{start_button_text}"/>
        </form>
    </body>
    </html>
    '''


@app.route('/product/<int:product_id>/star', methods=['post'])
def product_star_view(product_id: int):
    favorite_product_ids = session.get('favorite_product_ids', set())
    if product_id in favorite_product_ids:
        favorite_product_ids.remove(product_id)
    else:
        favorite_product_ids.add(product_id)
    session['favorite_product_ids'] = favorite_product_ids
    return redirect(f'/product/{product_id}')


if __name__ == '__main__':
    app.run(port=8080, debug=True)