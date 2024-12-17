import sys

from PySide6.QtWidgets import QApplication
from src.view.main_view import MainView
from src.controller.main_controller import MainController
from src.model.db_config import init_db
from src.services.client_service import ClientService, Client
from src.services.tool_service import ToolService, Tool
from src.services.employee_service import EmployeeService, Employee
from src.services.rent_agreement_service import RentAgreementService, RentAgreement
import src.model

if __name__ == "__main__":
    session = init_db("sqlite:///tools_db.sqlite")
    app = QApplication(sys.argv)
    view = MainView()
    controller = MainController(
        view, ClientService(session), ToolService(session),
        EmployeeService(session), RentAgreementService(session)
    )
    view.show()
    sys.exit(app.exec())

