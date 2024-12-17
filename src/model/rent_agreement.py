import datetime

from sqlalchemy import Column, Integer, Date, ForeignKey, String

from .db_config import Base


class RentAgreement(Base):
    __tablename__ = 'rent_agreement'

    id = Column(Integer, primary_key=True)
    conclusion_date = Column(Date, default=datetime.datetime.now)
    end_date = Column(Date)
    tool = Column(ForeignKey('tool.name'))
    employee = Column(ForeignKey('employee.id'))
    client = Column(ForeignKey('client.passport'))
    status = Column(String)
