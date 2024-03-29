from flask import Flask, Response
from starlette import status

from .cache import cache
from .endpoints.products import products

config = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
}

app = Flask(__name__)
app.config.from_mapping(config)
app.register_blueprint(products)

cache.init_app(app)


@app.get('/')
def main_url():
    return Response(status=status.HTTP_200_OK)
