from src.services.employee_service import EmployeeService
from src.services.client_service import ClientService
from src.services.tool_service import ToolService
from src.services.rent_agreement_service import RentAgreementService

from src import model
from src.model.db_config import init_db


import faker

fake = faker.Faker('ru_RU')
session = init_db("sqlite:///tools_db.sqlite")

service1 = EmployeeService(session)
for i in range(4):
    service1.add_employee(
        fake.name(),
        fake.phone_number(),
        fake.email(),
        fake.date_of_birth()
    )

tool_names = [
    "молоток",
    "дрель",
    "отвертка",
    "гайковерт",
    "пила",
    "шлифмашина",
    "лопата",
    "ножницы",
    "клещи",
    "рулетка"
]

tool_categories = [
    "ручной инструмент",
    "электроинструмент",
    "ручной инструмент",
    "электроинструмент",
    "ручной инструмент",
    "электроинструмент",
    "садовый инструмент",
    "ручной инструмент",
    "ручной инструмент",
    "ручной инструмент"
]

service2 = ToolService(session)
for i in range(10):
    try:
        service2.add_tool(
            name=tool_names[i],
            category=tool_categories[i],
            rent_cost=fake.random_int(min=10, max=100),
            amount=fake.random_int(min=1, max=10)
        )
    except:
        ...


def generate_passport():
    series = f"{fake.random_int(min=10, max=99)}{fake.random_int(min=10, max=99)}"
    number = f"{fake.random_int(min=100000, max=999999)}"
    passport = f"{series} {number}"
    return passport


service3 = ClientService(session)
for i in range(13):
    service3.add_client(
        passport=generate_passport(),
        fio=fake.name(),
        phone_number=fake.phone_number(),
        email=fake.email()
    )