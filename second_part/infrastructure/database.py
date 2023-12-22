from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine

from second_part.infrastructure.config import settings

engine = create_engine(settings.get_database_url, echo=False)
session_maker = sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
