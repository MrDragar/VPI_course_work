from PySide6.QtWidgets import QMainWindow, QDialog
from src.ui.clients_list_window import Ui_Dialog


class ClientView(QDialog):
    def __init__(self):
        super(ClientView, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
