from typing import Type

from sqlalchemy.orm import Session

from src.model.client import Client


class ClientService:
    __session: Session

    def __init__(self, session: Session):
        self.__session = session

    def add_client(
            self, passport: str, fio: str, phone_number: str, email: str
    ) -> None:

        client = Client(
            passport=passport or None, FIO=fio or None,
            phone_number=phone_number or None, email=email or None
        )
        self.__session.add(client)
        try:
            self.__session.commit()
        except Exception as ex:
            self.__session.rollback()
            raise ex

    def get_client_list(self) -> list[Type[Client]]:
        result = self.__session.query(Client).all()
        return result
