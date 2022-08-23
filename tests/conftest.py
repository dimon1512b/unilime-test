import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy_utils import database_exists, create_database

from app.config import settings
from app.main import app
from app.utils import create_db_if_not_exist


@pytest.fixture(scope="session")
def client():
    with app.test_client() as client:
        yield client


@pytest.fixture(scope="session")
def engine() -> create_engine:
    engine = create_engine(settings.DB_URL_TEST)
    return engine


@pytest.fixture(scope="session")
def session(engine) -> Session:
    with Session(engine) as session:
        return session


@pytest.fixture(autouse=True)
def creating_db(engine) -> None:
    create_db_if_not_exist(engine)


@pytest.fixture(autouse=True)
def fill_db(session) -> None:
    data = [
        {},
        {},
        {},
        {},
    ]
