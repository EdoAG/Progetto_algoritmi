from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('product', __name__)


@bp.route('/')
def index():
    db = get_db()
    products = db.execute(
        'SELECT p.id, title, body, created, author_id, username, prezzo, tags'
        ' FROM product p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    with open(r'C:\Users\EdoardoAndreaGiacomi\OneDrive - ITS Rizzoli\Desktop\Progetto_algoritmi-main\flask\flaskr\film.txt', 'r') as f: 
        return render_template('product/index.html', products=products, text=f.read())


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        prezzo = request.form['prezzo']
        tags = request.form['tags']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO product (title, body, prezzo, tags, author_id)'
                ' VALUES (?,?,?,?,?)',
                (title, body, prezzo, tags, g.user['id'])
            )
            db.commit()
            return redirect(url_for('product.index'))
    return render_template('product/create.html')


def get_product(id, check_author=True):
    product = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username, prezzo, tags'
        ' FROM product p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if product is None:
        abort(404, f"product id {id} doesn't exist.")

    if check_author and product['author_id'] != g.user['id']:
        abort(403)

    return product


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    product = get_product(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        prezzo = request.form['prezzo']
        tags = request.form['tags']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE product SET title = ?, body = ?, prezzo = ?, tags = ?'
                ' WHERE id = ?',
                (title, body, prezzo, tags, id)
            )
            db.commit()
            return redirect(url_for('product.index'))
    return render_template('product/update.html', product=product)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_product(id)
    db = get_db()
    db.execute('DELETE FROM product WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('product.index'))
