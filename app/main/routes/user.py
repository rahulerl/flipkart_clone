from flask import Blueprint
from ..services.user_service import *
import json

user = Blueprint('user', __name__)

@user.route('/registration', methods=['POST'])
def new_user():
    result = registration()
    if result:
        return json.dumps({'status': True, 'message': 'user added'})
    else:
        return json.dumps({'status': False, 'message': 'user not added'})


@user.route('/login', methods = ['POST'])
def log_in():
    status, message, token = login()
    return json.dumps({'status': status, 'message': message, 'token':token})


@user.route('/add_address', methods=['POST'])
def add_new_address():
    status, message = add_address()
    return json.dumps({'status': status, 'message': message})

@user.route('/add_to_cart', methods=['POST'])
def add_cart():
    status,msg = add_to_cart()
    return json.dumps({'status': status, 'message': msg})
@user.route('/make_an_order', methods=['POST'])
def ordr():
    status,msg = make_an_order()
    return json.dumps({'status': status, 'message': msg})


