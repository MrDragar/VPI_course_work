from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton

class AddRentAgreementView(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Добавить договор аренды")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Клиент
        self.client_label = QLabel("Клиент:")
        self.client_combo = QComboBox()
        layout.addWidget(self.client_label)
        layout.addWidget(self.client_combo)

        # Инструмент
        self.tool_label = QLabel("Инструмент:")
        self.tool_combo = QComboBox()
        layout.addWidget(self.tool_label)
        layout.addWidget(self.tool_combo)

        # Сотрудник
        self.employee_label = QLabel("Сотрудник:")
        self.employee_combo = QComboBox()
        layout.addWidget(self.employee_label)
        layout.addWidget(self.employee_combo)

        # Количество дней
        self.days_label = QLabel("Количество дней:")
        self.days_input = QLineEdit()
        layout.addWidget(self.days_label)
        layout.addWidget(self.days_input)

        # Кнопка "Добавить"
        self.submit_button = QPushButton("Добавить")
        layout.addWidget(self.submit_button)

        self.setLayout(layout)