from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIntValidator
from src.ui.tool_add_window import Ui_Dialog


class ToolAddView(QDialog):
    def __init__(self):
        super(ToolAddView, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.amount.setValidator(QIntValidator())
        self.ui.cost.setValidator(QIntValidator())

