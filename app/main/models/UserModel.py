from .. import db
import datetime
from ..models.ProductModel import Product


#treePath = db.Table('treePath',
 # db.Column('ancestor', db.Integer, db.ForeignKey('comments.comment_id'), primary_key=True),
 # db.Column('decendent', db.Integer, db.ForeignKey('comments.comment_id'), primary_key=True)
#)


class Users(db.Model):
    user_id = db.Column(db.String(50), primary_key=True)
    email = db.Column(db.String(50), unique=True,nullable=False)
    password = db.Column(db.String(50), nullable=False)
    user_type = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50))

class UserAddress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(500), nullable=False)
    address_type = db.Column(db.String(50))
    user_id = db.Column(db.String(50), db.ForeignKey('users.user_id'),nullable=False)

class MyCart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), db.ForeignKey('users.user_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
    usr = db.relationship("Users", foreign_keys=[user_id])
    product = db.relationship("Product", foreign_keys=[product_id])

class MyOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ammount = db.Column(db.Integer)
    payment_status = db.Column(db.String(20))
    payment_mode = db.Column(db.String(20))
    user_id = db.Column(db.String(50), db.ForeignKey('users.user_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
    usr = db.relationship("Users", foreign_keys=[user_id])
    product = db.relationship("Product", foreign_keys=[product_id])


#class Comments(db.Model):
 #   comment_id = db.Column(db.Integer, primary_key=True)
  #  author = db.Column(db.String(50), nullable=False)
   # comment = db.Column(db.String(500))
    #addresses = db.relationship('TreePath', backref='comment', lazy=True)
    #addresses1 = db.relationship('TreePath', backref='comment1', lazy=True)

    
   # treePath = db.relationship('Comments', secondary='TreePath', lazy='subquery',
    # backref=db.backref('comm', lazy=True))

#class TreePath(db.Model):
 #   ancestor = db.Column(db.Integer, db.ForeignKey('comments.comment_id'),primary_key=True)
  #  decendent = db.Column(db.Integer, db.ForeignKey('comments.comment_id'),primary_key=True)
   # company = db.relationship("Comments", foreign_keys=[ancestor])
    #stakeholder = db.relationship("Comments", foreign_keys=[decendent])


#class TreePath(db.Model):
 #   ancestor = db.Column(db.Integer, db.ForeignKey('comments.comment_id'),primary_key=True)
  #  decendent = db.Column(db.Integer, db.ForeignKey('comments.comment_id'),primary_key=True)