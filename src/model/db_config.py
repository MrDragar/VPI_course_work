from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session


# Базовый класс для моделей
Base = declarative_base()


def init_db(database_url) -> Session:
    # Создаем движок базы данных
    engine = create_engine(database_url, echo=True)
    Base.metadata.create_all(engine)
    # Создаем сессию для работы с базой данных
    db_session_creator = sessionmaker(bind=engine)
    session = db_session_creator()
    return session
