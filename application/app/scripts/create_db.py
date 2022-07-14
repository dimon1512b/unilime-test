from sqlalchemy import create_engine

from app.db.models import Base
from app.config import settings

user = settings.DB_USER
password = settings.DB_PASSWORD
db_name = settings.DB_NAME


engine = create_engine(
    f'postgresql://{user}:{password}@127.0.0.1:5432/{db_name}',
    echo=True,
)

Base.metadata.create_all(engine)
