from ..models.UserModel import *
from ..models.ProductModel import Product
from . import product_service
from flask import request
from . import auth


def registration():
    user_id = request.json['mobile_no']
    email = request.json['email']
    password = request.json['password']
    name = request.json['name']
    user_type = request.json['user_type']
    try:
        user = Users(user_id = user_id, email = email, password = password,
                name = name, user_type = user_type)
        db.session.add(user)
        db.session.commit()
        return True
    except:
        return False

def login():
    login_id = request.json['login_id']
    password = request.json['password']
    token = ''
    ans = []
    try:
        result = db.engine.execute("SELECT user_type FROM users WHERE user_id = '%s' AND password = '%s'"%(login_id, password));
        try:
            for i in result:
                ans = i
        except:
            False, 'invalid user', 'null'
        token = auth.getAuth(login_id, ans[0])
        return True, 'logged in', token
    except:
        return False, 'invalid user','null'


def add_to_cart():
    token = request.headers['Auth']
    user_id = request.json['user_id']
    product_id = request.json['product_id']
    status, msg, user_id = auth.verifyAuth(token)
    print("-------status ======", status)
    if status:
        try:
            result = MyCart(user_id = user_id, product_id = product_id)
            print("TRDFGHJLKJBHVBNM")
            db.session.add(result)
            db.session.commit()
            return True, 'item added to cart'
        except:
            return False, 'item not added to cart'
    else:
         return False, msg


def add_address():
    token = request.headers['Auth']
    address = request.json['address']
    address_type = request.json['address_type']
    usr_id = request.json['user_id']
    status, msg, user_id = auth.verifyAuth(token)
    if status:
        try:
            result = UserAddress(address = address, address_type = address_type, user_id = usr_id)
            db.session.add(result)
            db.session.commit()
            return True, 'address inserted'
        except:
            return False, 'address not inserted'
    else:
         return False, msg

def make_an_order():
    token = request.headers['Auth']
    ammount = request.json['ammount']
    payment_status = request.json['payment_status']
    payment_mode = request.json['payment_mode']
    user_id = request.json['user_id']
    product_id = request.json['product_id']
    status, msg, user_id = auth.verifyAuth(token)
    if status:
        try:
            result = MyOrder(ammount = ammount, product_id = product_id,payment_status = payment_status,
                         payment_mode = payment_mode,user_id = user_id)
            product_service.update_product_meta('remove',product_id)
            db.session.add(result)
            db.session.commit()
            return True, 'order completed'
        except:
            return False, 'order not completed'
    else:
         return False, msg