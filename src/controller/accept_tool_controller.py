from src.services.rent_agreement_service import RentAgreementService
from src.services.tool_service import ToolService
from src.view.accept_tool_view import AcceptToolView
from src.view.adapters import RentAgreementAdapter


class AcceptToolController:
    def __init__(self, view, main_controller, rent_agreement_service: RentAgreementService, tool_service: ToolService):
        self.main_controller = main_controller
        self.view: AcceptToolView = view
        self.rent_agreement_service = rent_agreement_service
        self.tool_service = tool_service

        # Заполняем комбобокс данными с использованием адаптера
        self.populate_combobox()

        # Подключаем кнопку "Принять"
        self.view.submit_button.clicked.connect(self.accept_tool)

        # Подключаем сигналы закрытия окна
        self.view.rejected.connect(self.on_close)  # При отмене
        self.view.accepted.connect(self.on_close)  # При подтверждении

    def show_window(self):
        self.view.exec()

    def populate_combobox(self):
        """Заполняет комбобокс данными с использованием адаптера."""
        agreements = self.rent_agreement_service.get_rent_agreement_list()
        for agreement in agreements:
            if agreement.status != 'open':
                continue
            adapter = RentAgreementAdapter(agreement)
            self.view.agreement_combo.addItem(adapter.text(), agreement.id)  # Сохраняем ID договора

    def accept_tool(self):
        try:
            # Получаем ID договора из комбобокса
            agreement_id = self.view.agreement_combo.currentData()  # Получаем сохраненный ID
            print(agreement_id, 1111111111)
            # Закрываем договор
            agreement = self.rent_agreement_service.close_rent(agreement_id)

            # Увеличиваем количество инструментов
            self.tool_service.change_amount(agreement.tool, 1)

            # Закрываем окно
            self.view.close()

        except Exception as e:
            raise e
            print(f"Ошибка: {e}")

    def on_close(self):
        """Метод, вызываемый при закрытии окна."""
        self.main_controller.enable_window()  # Разблокируем основное окно