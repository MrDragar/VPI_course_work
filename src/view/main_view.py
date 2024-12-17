from PySide6.QtWidgets import QMainWindow
from src.ui.mainwindow import Ui_MainWindow


class MainView(QMainWindow):
    def __init__(self):

        super(MainView, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

