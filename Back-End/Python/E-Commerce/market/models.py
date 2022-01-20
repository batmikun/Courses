from market import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    barcode = db.Column(db.String(10), nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)
    descripction = db.Column(db.String(1024))

    def __init__(self, name, price, barcode, description):
        self.name = name
        self.price = price
        self.barcode = barcode
        self.descripction = description

    def __repr__(self):
        return f'Item {self.name}'
