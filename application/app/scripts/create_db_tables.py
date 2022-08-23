from sqlalchemy import create_engine

from app.db.models import Base
from app.config import settings
from app.utils import create_db_if_not_exist

user = settings.DB_USER
password = settings.DB_PASSWORD
db_name = settings.DB_NAME

"""
    For this test project enough just create db
    But for another projects need to use Flask-Migrate & Flask-SQLAlchemy
    or pure SQLAlchemy & pure Alembic
"""


engine = create_engine(
    settings.DB_URL_SYNC,
    echo=True,
)

create_db_if_not_exist(engine)

Base.metadata.create_all(engine)
