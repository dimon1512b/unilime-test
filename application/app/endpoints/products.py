from flask import Blueprint, request
from pydantic import PositiveInt

products = Blueprint('products', __name__, url_prefix='/products')


@products.route('/get_product', methods=['GET'])
async def get_product():
    return 'Get product'


@products.route('/set_review', methods=['PUT'])
async def set_review() -> str:
    return f'Set product by id {request.form.get("product_id")}'
