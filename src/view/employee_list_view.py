from PySide6.QtWidgets import QDialog, QVBoxLayout, QListWidget


class EmployeeListView(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Список сотрудников")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        self.setLayout(layout)