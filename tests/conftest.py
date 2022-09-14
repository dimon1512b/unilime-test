import random

import pytest
from flask import Flask

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import Session, sessionmaker

from app.config import settings
from app.db.models import Base, Product, Review
from app.main import app
from app.utils import create_db_if_not_exist


@pytest.fixture(autouse=True)
def patched_db(mocker):
    async_engine = create_async_engine(
        settings.DB_URL_TEST_A,
        future=True,
        echo=settings.DB_DEBUG,
        pool_pre_ping=True,
        pool_use_lifo=True,
        pool_recycle=settings.DB_POOL_RECYCLE,
    )
    session_local = sessionmaker(
        async_engine,
        expire_on_commit=False,
        class_=AsyncSession,
    )

    mocker.patch(
        'app.utils.session_local',
        session_local,
    )


@pytest.fixture(scope="session")
def client() -> Flask:
    return app.test_client()


@pytest.fixture(scope="session")
def engine() -> create_engine:
    engine = create_engine(settings.DB_URL_TEST)

    return engine


@pytest.fixture(scope="session")
def db_session(engine) -> Session:
    with Session(engine) as session:
        return session


@pytest.fixture(autouse=True, scope='session')
def creating_db(engine) -> None:
    create_db_if_not_exist(engine)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    yield

    Base.metadata.drop_all(engine)


@pytest.fixture
def product(
    db_session: Session,
) -> Product:
    product = Product(
        asin=str(random.randint(1000, 9999)),
        title='title'
    )
    db_session.add(product)
    db_session.commit()

    yield product

    db_session.delete(product)
    db_session.commit()


@pytest.fixture
def review(
    product: Product,
    db_session: Session,
) -> Review:
    review = Review(
        title='title',
        text='review text',
        product_asin=product.asin,
    )
    db_session.add(review)
    db_session.commit()

    yield review

    db_session.delete(review)
    db_session.commit()
