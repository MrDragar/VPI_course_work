import datetime
from typing import Type

from sqlalchemy.orm import Session

from src.model.employee import Employee


class EmployeeService:
    __session: Session

    def __init__(self, session: Session):
        self.__session = session

    def get_employee_list(self) -> list[Type[Employee]]:
        return self.__session.query(Employee).all()

    def add_employee(
            self, fio: str, phone: str, email: str,
            birthday: datetime.datetime
    ) -> None:
        self.__session.add(
            Employee(
                FIO=fio or None, phone_number=phone or None,
                email=email or None, birthday=birthday or None
            )
        )
        try:
            self.__session.commit()
        except:
            self.__session.rollback()
            raise
