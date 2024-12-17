from PySide6.QtWidgets import QMainWindow, QDialog
from src.ui.clients_list_window import Ui_Dialog


class ToolListView(QDialog):
    def __init__(self):
        super(ToolListView, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
