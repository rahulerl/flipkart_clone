from .. import db
import datetime

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), nullable=False)

class TreePath(db.Model):
    ancestor = db.Column(db.Integer, db.ForeignKey('category.id'),primary_key=True)
    decendent = db.Column(db.Integer, db.ForeignKey('category.id'),primary_key=True)
    ancestor_rel = db.relationship("Category", foreign_keys=[ancestor])
    decendent_rel = db.relationship("Category", foreign_keys=[decendent])

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    product_category = db.Column(db.String(100), nullable=False)
    product_cat_id = db.Column(db.Integer, db.ForeignKey('category.id'))

class Product_meta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(100))
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(100))
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
