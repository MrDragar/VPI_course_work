from sqlalchemy import Column, String

from .db_config import Base


class Client(Base):
    __tablename__ = 'client'

    passport = Column(String, primary_key=True, nullable=False)
    FIO = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def __str__(self):
        return f"{self.FIO} {self.phone_number} {self.email} {self.passport}"