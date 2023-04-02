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
        return [Product(*row) for row in rows.fetchall()]


def get_product(product_id: int) -> Product:
    with sqlite3.connect(DATABASE_FILE) as connection:
        rows = connection.execute(
            'SELECT id, name, description, category FROM product WHERE id = ?',
            (product_id,)).fetchall()
        assert len(rows) == 1
        return Product(*rows[0])


def get_products_by_ids(product_ids: set) -> list[Product]:
    with sqlite3.connect(DATABASE_FILE) as connection:
        product_ids_str = ','.join(str(product_id) for product_id in product_ids)
        rows = connection.execute(
            f'SELECT id, name, description, category FROM product WHERE id IN ({product_ids_str})')
        return [Product(*row) for row in rows.fetchall()]


def generate_html_list(products: list[Product]) -> str:
    list_html = '\n'.join(
        f'<li><a href="/product/{product.id}">{product.name}</a></li>'
        for product in products)
    return f'<ul>{list_html}</ul>'


@app.route('/products')
def products_view():
    products = load_products()
    products_html = generate_html_list(products)
    return f'''
    <html>
    <head>
        <title>Shop APP</title>
    </head>
    <body>
        <h1><a href="/favorite-products">Go to favorite products page</a></h1>
        <h1>Products</h1>
        {products_html}
    </body>
    </html>
    '''


@app.route('/product/<int:product_id>')
def product_view(product_id: int):
    favorite_product_ids = session.get('favorite_product_ids', set())

    product = get_product(product_id)
    product_name = product.name
    is_favorite = product.id in favorite_product_ids
    if is_favorite:
        product_name += ' &#10027;'
    star_button_title = 'Remove from favorites' if is_favorite else 'Add to favorites'
    return f'''
    <html>
    <head>
        <title>Shop APP</title>
    </head>
    <body>
        <h1><a href="/products">Go to all products page</a></h1>
        <h1><a href="/favorite-products">Go to favorite products page</a></h1>
        <h1>{product_name} </h1>
        <h2>Category: {product.category}</h2>
        <p>{product.description}</p>
        <form action="/product/{product.id}/star" method="post">
            <input type="Submit" value="{star_button_title}"/>
        </form>
    </body>
    </html>
    '''


@app.route('/product/<int:product_id>/star', methods=['post'])
def star_product(product_id: int):
    favorite_product_ids = session.get('favorite_product_ids', set())
    product = get_product(product_id)
    if product.id in favorite_product_ids:
        favorite_product_ids.remove(product.id)
    else:
        favorite_product_ids.add(product.id)
    session['favorite_product_ids'] = favorite_product_ids
    return redirect(f'/product/{product.id}')


@app.route('/favorite-products')
def favorite_products_view():
    favorite_products_ids = session.get('favorite_product_ids', set())
    favorite_products = get_products_by_ids(favorite_products_ids)
    products_html = generate_html_list(favorite_products) \
        if len(favorite_products) > 0 \
        else 'You have not chosen favorite products'
    return f'''
    <html>
    <head>
        <title>Shop APP</title>
    </head>
    <body>
        <h1><a href="/products">Go to all products page</a></h1>
        <h1>Favorite Products</h1>
        {products_html}
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(port=8080, debug=True)
