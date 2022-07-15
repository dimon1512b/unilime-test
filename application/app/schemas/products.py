from typing import Optional

from pydantic import BaseModel, PositiveInt


class GetProductReviewReq(BaseModel):
    product_id: PositiveInt
    limit: Optional[PositiveInt]
    offset: Optional[PositiveInt]


class SetReview(BaseModel):
    product_id: PositiveInt
    title: Optional[str]
    review: str
