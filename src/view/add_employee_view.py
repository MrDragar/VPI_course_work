from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QDateEdit


class AddEmployeeView(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Добавить сотрудника")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.fio_label = QLabel("ФИО:")
        self.fio_input = QLineEdit()
        layout.addWidget(self.fio_label)
        layout.addWidget(self.fio_input)

        self.phone_label = QLabel("Телефон:")
        self.phone_input = QLineEdit()
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_input)

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)

        self.birthday_label = QLabel("Дата рождения:")
        self.birthday_input = QDateEdit()
        layout.addWidget(self.birthday_label)
        layout.addWidget(self.birthday_input)

        self.submit_button = QPushButton("Добавить")
        layout.addWidget(self.submit_button)

        self.setLayout(layout)
