from second_part.infrastructure.database import Base, engine, session_maker
from second_part.infrastructure.models.users import Users
from second_part.infrastructure.models.messages import Messages
from sqlalchemy import insert, select


def create_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def insert_values_in_users():
    with session_maker() as session:
        query = insert(Users).values(
            [
                {"user": "user1", "datastr": "231220122530"},
                {"user": "user1", "datastr": "231219111015"},
                {"user": "user1", "datastr": "231218191510"},
                {"user": "user1", "datastr": "231217212023"},
                {"user": "user1", "datastr": "231216155055"},
                {"user": "user1", "datastr": "231225093305"},
                {"user": "user1", "datastr": "231224231322"},
                {"user": "user1", "datastr": "231223231322"},
                {"user": "user1", "datastr": "231221231322"},
                {"user": "user1", "datastr": "231222001223"},
                {"user": "user2", "datastr": "231216155055"},
                {"user": "user2", "datastr": "231215093305"},
                {"user": "user2", "datastr": "231214231322"},
                {"user": "user3", "datastr": "231214231322"},
            ])
        session.execute(query)
        session.commit()


def get_distinct_users():
    with session_maker() as session:
        query = select(Users.user).select_from(Users).distinct()
        result = session.execute(query)
        return result.scalars().all()


def get_datastr_for_user(user):
    with session_maker() as session:
        query = select(Users.datastr).where(Users.user == user)
        result = session.execute(query)
        return result.scalars().all()


def insert_message(**data):
    with session_maker() as session:
        query = insert(Messages).values(**data)
        session.execute(query)
        session.commit()
