import datetime
from typing import Type

from sqlalchemy.orm import Session

from src.model import Client
from src.model.employee import Employee
from src.model.rent_agreement import RentAgreement
from src.model.tool import Tool


class RentAgreementService:
    __session: Session

    def __init__(self, session: Session):
        self.__session = session

    def get_rent_agreement_list(self) -> list[Type[RentAgreement]]:
        return self.__session.query(RentAgreement).all()

    def add_rent_agreement(
            self, days: int, tool_name: int, employee_id: int, client_passport: int
    ) -> None:
        start_date = datetime.datetime.now()
        end_date = start_date + datetime.timedelta(days=days)

        employee: Employee = self.__session.query(Employee).get(employee_id)
        tool: Tool = self.__session.query(Tool).get(tool_name)
        client: Client = self.__session.query(Client).get(client_passport)

        self.__session.add(
            RentAgreement(
                conclusion_date=start_date or None, end_date=end_date or None, tool=tool.name or None,
                employee=employee.id or None, status='open', client=client.passport or None
            )
        )
        try:
            self.__session.commit()
        except:
            self.__session.rollback()
            raise

    def close_rent(self, id: int) -> RentAgreement:
        rent: RentAgreement = self.__session.query(RentAgreement).get(id)
        rent.status = 'close'
        self.__session.commit()
        return rent
