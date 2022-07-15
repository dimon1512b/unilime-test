import json

from flask import Blueprint, request

from app.schemas.products import GetProductReviewReq, SetReview
from app.utils import get_request, product_reviews, set_new_review

products = Blueprint('products', __name__, url_prefix='/products')


@products.route('/get_product_review', methods=['POST', 'GET'])
async def get_product_review() -> json:
    """
    Parameters
    ----------
    product_id: int
    limit: int = 10
    offset: int = 0

    Returns
    -------
    json
        a json with static keys "asin: product.asin", "title: product.title"
        and different "review_title: review.title", "review: review.text"
        depending on limit & offset
    """
    req = get_request(request)
    try:
        if GetProductReviewReq(**req):
            return json.dumps(await product_reviews(req))
    except Exception as e:
        return json.dumps({
            "status": "failure",
            "reason": str(e),
        })


@products.route('/set_review', methods=['POST', 'PUT'])
async def set_review() -> str:
    """
        Parameters
        ----------
        product_id: int
        title: str = None
        review: str

        Returns
        -------
        '{"status": "success"}' or '{"status": "failure", "reason":"reason"}'
        """
    req = get_request(request)
    try:
        print(f'{req = }')
        if SetReview(**req):
            await set_new_review(req)
            return json.dumps({"status": "success"})
    except Exception as e:
        return json.dumps({
            "status": "failure",
            "reason": str(e),
        })
    return json.dumps(req)
