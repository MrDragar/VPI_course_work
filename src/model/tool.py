from sqlalchemy import Column, Integer, String

from .db_config import Base


class Tool(Base):
    __tablename__ = 'tool'

    name = Column(String, primary_key=True)
    category = Column(String, nullable=False)
    rent_cost = Column(Integer)
    amount = Column(Integer)

    def __str__(self):
        return f"{self.name} {self.category} {self.rent_cost} {self.amount}"