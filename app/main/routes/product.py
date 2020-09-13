from flask import Blueprint
from ..services.product_service import *
import json

product = Blueprint('product', __name__)

@product.route('/add_category', methods=['POST'])
def add_categories():
        result = add_category()
        if result:
            return json.dumps({'status': True, 'message': 'category added'})
        else:
            return json.dumps({'status': False, 'message': 'category not added'})


@product.route('/get_subcategory', methods=['GET'])
def get_subCat():
    status, Category = get_subcategory()
    return json.dumps({'status': status, 'category': Category})

@product.route('/add_product', methods=['POST'])
def add_prod():
    result = add_product()
    if result:
        return json.dumps({'status': True, 'message': 'product added'})
    else:
        return json.dumps({'status': False, 'message': 'product not added'})


@product.route('/add_meta', methods=['POST'])
def add_meta():
    result = add_meta_data()
    if result:
        return json.dumps({'status': True, 'message': 'product_mata added'})
    else:
        return json.dumps({'status': False, 'message': 'product_meta not added'})


@product.route('/get_product_by_type', methods=['GET'])
def get_prod():
    status,result = get_product_by_type()
    return json.dumps({'status': status, 'data': result})


@product.route('/get_product_by_filter', methods=['GET'])
def get_filder_prod():
    status,result = get_product_by_filter()
    return json.dumps({'status': status, 'data': result})