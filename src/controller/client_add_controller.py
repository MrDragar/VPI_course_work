from src.view.client_add_dialog_view import ClientAddView
from src.services.client_service import ClientService


class ClientAddController:
    def __init__(self, view, main_controller, client_service: ClientService):
        self.main_controller = main_controller
        self.view: ClientAddView = view
        self.client_service = client_service
        self.view.rejected.connect(self.open_main_window)
        # self.view.ui.buttonBox.accepted.connect(self.save_client)
        self.view.accept = self.save_client

    def show_client_window(self):
        self.view.exec()

    def save_client(self):
        print("save")
        passport = self.view.ui.passport.text()
        fio = self.view.ui.fio.text()
        phone_number = self.view.ui.phone.text()
        email = self.view.ui.email.text()
        try:
            self.client_service.add_client(passport, fio, phone_number, email)
        except Exception as ex:
            print(ex)
            return
        print(5)
        self.view.close()
        self.main_controller.enable_window()

    def open_main_window(self):
        self.main_controller.enable_window()
