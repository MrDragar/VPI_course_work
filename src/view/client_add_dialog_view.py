from PySide6.QtWidgets import QMainWindow, QDialog
from src.ui.clients_add_window import Ui_Dialog


class ClientAddView(QDialog):
    def __init__(self):
        super(ClientAddView, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # self.ui.buttonBox.accepted.disconnect(self.accept)
