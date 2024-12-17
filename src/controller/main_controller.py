from src.services.client_service import ClientService
from src.services.employee_service import EmployeeService
from src.services.rent_agreement_service import RentAgreementService
from src.services.tool_service import ToolService
from src.view.client_add_dialog_view import ClientAddView
from src.view.client_list_view import ClientView
from src.view.tool_list_view import ToolListView
from src.view.tool_add_dialog_view import ToolAddView
from src.view.main_view import MainView
from .add_employee_controller import AddEmployeeController
from .agreements_controller import AgreementsController
from .client_add_controller import ClientAddController
from .client_list_controller import ClientListController
from .employee_list_controller import EmployeeListController
from .tool_list_controller import ToolListController
from .tool_add_controller import ToolAddController
from .accept_tool_controller import AcceptToolController
from .add_rent_agreement_controller import AddRentAgreementController
from src.view.add_rent_agreement_view import AddRentAgreementView
from src.view.accept_tool_view import AcceptToolView
from src.view.agreements_view import AgreementsView
from src.view.employee_list_view import EmployeeListView
from src.view.add_employee_view import AddEmployeeView


class MainController:
    client_service: ClientService
    employee_service: EmployeeService
    rent_agreement_service: RentAgreementService
    tool_service: ToolService

    def __init__(
            self, view, client_service, tool_service,
            employee_service, rent_agreement_service
    ):
        self.view: MainView = view
        self.client_service = client_service
        self.employee_service = employee_service
        self.rent_agreement_service = rent_agreement_service
        self.tool_service = tool_service

        self.view.ui.list_client_button.clicked.connect(self.show_client_window)
        self.view.ui.add_client_button.clicked.connect(self.add_client_window)
        self.view.ui.instrument_list_button.clicked.connect(self.show_tool_window)
        self.view.ui.add_instrument_button.clicked.connect(self.add_tool_window)
        self.view.ui.give_tool_button.clicked.connect(self.give_tool_window)
        self.view.ui.accept_tool_button.clicked.connect(self.accept_tool_window)
        self.view.ui.agreements_button.clicked.connect(self.agreements_window)
        self.view.ui.employee_list_button.clicked.connect(self.show_employee_list_window)
        self.view.ui.add_employee_button.clicked.connect(self.add_employee_window)

    def show_client_window(self):
        client_controller = ClientListController(
            ClientView(), self, self.client_service
        )
        self.view.setDisabled(True)
        client_controller.show_client_window()

    def add_client_window(self):
        controller = ClientAddController(
            ClientAddView(), self, self.client_service
        )
        self.view.setDisabled(True)
        controller.show_client_window()

    def show_tool_window(self):
        controller = ToolListController(
            ToolListView(), self, self.tool_service
        )
        self.view.setDisabled(True)
        controller.show_tool_window()

    def add_tool_window(self):
        controller = ToolAddController(
            ToolAddView(), self, self.tool_service
        )
        self.view.setDisabled(True)
        controller.show_tool_window()

    def enable_window(self):
        self.view.setDisabled(False)

    def give_tool_window(self):
        controller = AddRentAgreementController(
            AddRentAgreementView(), self,
            self.client_service, self.tool_service, self.employee_service,
            self.rent_agreement_service
        )
        self.view.setDisabled(True)
        controller.show_window()

    def accept_tool_window(self):
        controller = AcceptToolController(
            AcceptToolView(), self,
            self.rent_agreement_service, self.tool_service
        )
        self.view.setDisabled(True)
        controller.show_window()

    def agreements_window(self):
        controller = AgreementsController(
            AgreementsView(), self, self.rent_agreement_service
        )
        self.view.setDisabled(True)
        controller.show_window()

    def show_employee_list_window(self):
        controller = EmployeeListController(
            EmployeeListView(), self, self.employee_service
        )
        self.view.setDisabled(True)
        controller.show_window()
    
    def add_employee_window(self):
        controller = AddEmployeeController(
            AddEmployeeView(), self, self.employee_service
        )
        self.view.setDisabled(True)
        controller.show_window()