from market import app
from market.models import Item
from flask import render_template


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('pages/home.html')


@app.route('/market')
def market():

    items = Item.query.all()

    return render_template('pages/market.html', items=items)
