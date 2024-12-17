from typing import Type

from sqlalchemy.orm import Session

from src.model.tool import Tool


class ToolService:
    __session: Session

    def __init__(self, session: Session):
        self.__session = session

    def get_tool_list(self) -> list[Type[Tool]]:
        return self.__session.query(Tool).all()

    def add_tool(
            self, name: str, category: str, rent_cost: int,
            amount:  int
    ) -> None:
        self.__session.add(
            Tool(
                name=name or None, category=category or None,
                rent_cost=rent_cost or None, amount=amount or None
            )
        )
        try:
            self.__session.commit()
        except:
            self.__session.rollback()
            raise

    def change_amount(self, name: str, diff: int) -> None:
        tool: Tool = self.__session.query(Tool).get(name)
        tool.amount += diff
        self.__session.commit()
