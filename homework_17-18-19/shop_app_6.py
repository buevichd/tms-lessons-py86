import sqlite3
from dataclasses import dataclass, field
from flask import Flask, session, redirect
from flask_session import Session


DATABASE_FILE = 'db_6.sqlite3'

app = Flask(__name__)
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


@dataclass
class Product:
    id: int
    name: str
    description: str
    category_id: int


@dataclass
class Category:
    id: int
    name: str
    products: list[Product] = field(default_factory=list)


def load_products() -> list[Product]:
    with sqlite3.connect(DATABASE_FILE) as connection:
        rows = connection.execute('SELECT id, name, description, category_id FROM product')
        return [Product(*row) for row in rows.fetchall()]


def load_product(product_id: int) -> Product:
    with sqlite3.connect(DATABASE_FILE) as connection:
        rows = connection.execute(
            'SELECT id, name, description, category_id FROM product WHERE id = ?',
            (product_id,)).fetchall()
        assert len(rows) == 1
        return Product(*rows[0])


def load_products_by_ids(product_ids: set) -> list[Product]:
    with sqlite3.connect(DATABASE_FILE) as connection:
        product_ids_str = ','.join(str(product_id) for product_id in product_ids)
        rows = connection.execute(
            f'SELECT id, name, description, category_id FROM product WHERE id IN ({product_ids_str})')
        return [Product(*row) for row in rows.fetchall()]


def load_products_by_category_id(category_id: int):
    with sqlite3.connect(DATABASE_FILE) as connection:
        rows = connection.execute(
            f'SELECT id, name, description, category_id FROM product WHERE category_id = ?',
            (category_id,))
        return [Product(*row) for row in rows.fetchall()]


def load_category(category_id: int) -> Category:
    with sqlite3.connect(DATABASE_FILE) as connection:
        rows = connection.execute(
            'SELECT id, name FROM category WHERE id = ?',
            (category_id,)).fetchall()
        assert len(rows) == 1
        return Category(*rows[0])


def load_all_categories_with_products() -> list[Category]:
    with sqlite3.connect(DATABASE_FILE) as connection:
        rows = connection.execute(
            'SELECT product.id, product.name, product.description, product.category_id, category.id, category.name '
            'FROM category '
            'JOIN product ON category.id = product.category_id'
        )
        categories = {}
        for row in rows:
            category_id = row[4]
            if category_id not in categories:
                categories[category_id] = Category(category_id, row[5])
            category = categories[category_id]
            category.products.append(Product(*row[:4]))
        return list(categories.values())


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
        <h1><a href="/">Go to main page</a></h1>
        <h1><a href="/favorite-products">Go to favorite products page</a></h1>
        <h1>Products</h1>
        {products_html}
    </body>
    </html>
    '''


@app.route('/product/<int:product_id>')
def product_view(product_id: int):
    favorite_product_ids = session.get('favorite_product_ids', set())

    product = load_product(product_id)
    category = load_category(product.category_id)
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
        <h1><a href="/">Go to main page</a></h1>
        <h1><a href="/products">Go to all products page</a></h1>
        <h1><a href="/favorite-products">Go to favorite products page</a></h1>
        <h1>{product_name} </h1>
        <h2>Category: <a href="/category/{category.id}">{category.name}</a></h2>
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
    product = load_product(product_id)
    if product.id in favorite_product_ids:
        favorite_product_ids.remove(product.id)
    else:
        favorite_product_ids.add(product.id)
    session['favorite_product_ids'] = favorite_product_ids
    return redirect(f'/product/{product.id}')


@app.route('/favorite-products')
def favorite_products_view():
    favorite_products_ids = session.get('favorite_product_ids', set())
    favorite_products = load_products_by_ids(favorite_products_ids)
    products_html = generate_html_list(favorite_products) \
        if len(favorite_products) > 0 \
        else 'You have not chosen favorite products'
    return f'''
    <html>
    <head>
        <title>Shop APP</title>
    </head>
    <body>
        <h1><a href="/">Go to main page</a></h1>
        <h1><a href="/products">Go to all products page</a></h1>
        <h1>Favorite Products</h1>
        {products_html}
    </body>
    </html>
    '''


@app.route('/category/<int:category_id>')
def category_view(category_id: int):
    category = load_category(category_id)
    category.products = load_products_by_category_id(category_id)
    products_html = generate_html_list(category.products)
    return f'''
    <html>
    <head>
        <title>Shop APP</title>
    </head>
    <body>
        <h1><a href="/">Go to main page</a></h1>
        <h1><a href="/products">Go to all products page</a></h1>
        <h1><a href="/favorite-products">Go to favorite products page</a></h1>
        <h1>{category.name}</h1>
        {products_html}
    </body>
    </html>
    '''


@app.route('/')
def main_page_view():
    categories = load_all_categories_with_products()
    categories_html = '\n'.join(
        f'<li>'
        f'    <a href="/category/{category.id}">{category.name}</a>'
        f'    {generate_html_list(category.products)}'
        f'</li>'
        for category in categories)
    return f'''
    <html>
    <head>
        <title>Shop APP</title>
    </head>
    <body>
        <h1><a href="/products">Go to all products page</a></h1>
        <h1><a href="/favorite-products">Go to favorite products page</a></h1>
        <h1>Main Page</h1>
        <ul>
            {categories_html}
        </ul>
    </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(port=8080, debug=True)
