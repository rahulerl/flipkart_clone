from ..models.ProductModel import *
from flask import request
from . import auth

def add_category():
    token = request.headers['Auth']
    category = request.json['category']
    status, msg, user_id = auth.verifyAuth(token)
    if msg == 'admin' or msg == 'owner':
        try:
            cat = Category(category = category)
            db.session.add(cat)
            db.session.commit()
            return True
        except:
            return False
    else:
        return False

def get_subcategory():
    token = request.headers['Auth']
    category = request.json['category']
    status, msg, user_id = auth.verifyAuth(token)
    if status:
        try:
            result = db.engine.execute("SELECT c.* FROM category c JOIN tree_path t ON (c.id = t.decendent) where t.ancestor IN (SELECT id from category where category = '%s')"%(category));
            ans = []
            for i in result:
                ans.append({"id":i[0], "sub_category":i[1]})
            return True, ans
        except:
            return False, []
    else:
        return False, []

def add_product():
    token = request.headers['Auth']
    product_name = request.json['product_name']
    product_category = request.json['product_category']
    Category_id = request.json['category_id']
    status, msg, user_id = auth.verifyAuth(token)
    if msg == 'owner':
        try:
            pro = Product(product_name = product_name,product_category = product_category,
                     product_cat_id = Category_id)
            db.session.add(pro)
            db.session.commit()
            return True
        except:
            return False
    else:
        return False

def add_meta_data():
    token = request.headers['Auth']
    image_url = request.json['image_url']
    price = request.json['price']
    description = request.json['description']
    product_id = request.json['product_id']
    quantity = request.json['quantity']
    status, msg, user_id = auth.verifyAuth(token)
    if msg == 'owner':
        try:
            meta = Product_meta(image_url = image_url,price = price, description = description,
                     quantity = quantity,product_id = product_id)
            db.session.add(meta)
            db.session.commit()
            return True
        except:
           return False
    else:
        return False

def get_product_by_type():
    token = request.headers['Auth']
    product_type = request.json['product_type']
    page_no = request.json['page_no']
    status, msg, user_id = auth.verifyAuth(token)
    if status:
        try:
            result = db.engine.execute("SELECT product.product_name,product_meta.image_url,product_meta.price,product_meta.description FROM product JOIN product_meta ON (product.product_id = product_meta.product_id) WHERE product.product_category = '%s' limit %s,2;"%(product_type,page_no));
            ans = []
            for i in result:
                ans.append({"product_name":i[0], " image_url":i[1], "price":i[2],"description":i[3]})
            return True, ans
        except:
            return False, []
    else:
        return False, []

def get_product_by_filter():
    token = request.headers['Auth']
    category_id = request.json['category_id']
    page_no = request.json['page_no']
    status, msg, user_id = auth.verifyAuth(token)
    if status:
        try:
            result = db.engine.execute("SELECT product.product_name,product_meta.image_url,product_meta.price,product_meta.description FROM product JOIN product_meta ON (product.product_id = product_meta.product_id) WHERE product.product_cat_id = %s limit %s,2"%(category_id,page_no));
            ans = []
            for i in result:
                ans.append({"product_name":i[0], " image_url":i[1], "price":i[2],"description":i[3]})
            return True, ans
        except:
            return False, []
    else:
        return False, []


def update_product_meta(operation,product_id):
    if operation == 'add':
        try:
            result = db.engine.execute("UPDATE product_meta SET quantity = quantity + 1 WHERE product_id = %s"%(product_id));
            return True
        except:
            return False
    else:
        try:
            result = db.engine.execute("UPDATE product_meta SET quantity = quantity - 1 WHERE product_id = %s"%(product_id));
            return True
        except:
            return False