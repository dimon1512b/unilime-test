from flask import Blueprint, request

products = Blueprint('products', __name__, url_prefix='/products')


@products.route('/get_product_review', methods=['GET'])
async def get_product():
    """
    Parameters
    ----------
    product_id: int
    limit: int
    offset: int

    Returns
    -------
    json
        a json with static keys "asin: product.asin", "title: product.title"
        and different "review_title: review.title", "review: review.text"
        depending on limit & offset
    """
    return 'Get product review'


@products.route('/set_review', methods=['PUT'])
async def set_review() -> str:
    return f'Set product by id {request.form.get("product_id")}'
