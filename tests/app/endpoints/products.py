import pytest
from starlette import status


@pytest.mark.parametrize(
    "product_id, limit, offset, is_error_expected",
    [
        (),
        (),
        (),
    ]
)
async def test_get_product_review(
    client,
    product_id,
    limit,
    offset,
    is_error_expected,
):
    pass
