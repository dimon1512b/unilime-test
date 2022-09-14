"""One test for example"""

import asyncio
import json

from flask import Flask

from starlette import status

from app.db.models import Review, Product


async def test_get_product_review(
    client: Flask,
    product: Product,
    review: Review,
):

    def sync_test():
        res = client.get(
            f'/products/get_product_review?product_id={product.id}')

        assert res.status_code == status.HTTP_200_OK
        assert json.loads(res.text) == {
            "asin": product.asin,
            "title": product.title,
            "reviews": [{"review_title": review.title, "review": review.text}]
        }

    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, sync_test)
