from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QPushButton


class AcceptToolView(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Принять инструмент")
        self.setGeometry(100, 100, 400, 200)

        # Основной макет
        layout = QVBoxLayout()

        # Метка и комбобокс для выбора договора аренды
        self.agreement_label = QLabel("Договор аренды:")
        self.agreement_combo = QComboBox()
        layout.addWidget(self.agreement_label)
        layout.addWidget(self.agreement_combo)

        # Кнопка "Принять"
        self.submit_button = QPushButton("Принять")
        layout.addWidget(self.submit_button)

        # Устанавливаем макет
        self.setLayout(layout)