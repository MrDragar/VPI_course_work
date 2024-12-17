from sqlalchemy import Column, Integer, String, Date

from .db_config import Base


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True)
    FIO = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    email = Column(String, nullable=False)
    birthday = Column(Date, nullable=False)
