import asyncio

from sqlalchemy import select

from app.db.models import Product, Review
from app.db.session import session_local


def get_request(request) -> dict:
    if request.method in ['PUT', 'POST']:
        return request.get_json()
    elif request.method == 'GET':
        return request.args


async def get_product_by_id(data) -> Product:
    async with session_local() as session:
        product_obj = await session.execute(
            select(Product)
            .where(Product.id == int(data['product_id']))
        )
        return product_obj.scalars().one()


async def product_reviews(data: dict) -> dict:
    res = dict()
    async with session_local() as session:
        product = await get_product_by_id(data)

        res["asin"] = product.asin  # noqa
        res["title"] = product.title
        res["reviews"] = []
        review_obj = await session.execute(
            select(Review)
            .where(Review.product_asin == product.asin)
            .order_by(Review.id)
            .limit(data.get("limit", 10))
            .offset(data.get("offset", 0))
        )
        reviews = review_obj.scalars().all()
        for review in reviews:
            res["reviews"].append({
                'review_title': review.title,
                'review': review.text,
            })
    return res


async def set_new_review(data: dict) -> None:
    product = await get_product_by_id(data)
    async with session_local() as session:
        new_review = Review(
            title=data.get("title"),
            text=data["review"],
            product_asin=product.asin,
        )
        session.add(new_review)
        await session.commit()
        print(f'{new_review.__dict__ = }')
