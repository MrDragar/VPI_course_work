import PySide6.QtWidgets

from src.model.client import Client
from src.view.client_list_view import ClientView
from src.services.client_service import ClientService


class ClientAdapter(PySide6.QtWidgets.QListWidgetItem):
    def __init__(self, client: Client):
        super().__init__()
        self.client = client
        self.setText(str(client))


class ClientListController:
    def __init__(self, view, main_controller, client_service: ClientService):
        self.main_controller = main_controller
        self.view: ClientView = view
        self.client_service = client_service
        self.view.accepted.connect(self.open_main_window)
        self.view.rejected.connect(self.open_main_window)

    def show_client_window(self):
        clients = self.client_service.get_client_list()

        for client in clients:
            self.view.ui.listWidget.addItem(ClientAdapter(client))
        self.view.exec()

    def open_main_window(self):
        self.main_controller.enable_window()
