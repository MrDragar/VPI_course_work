from src.services.client_service import ClientService
from src.services.employee_service import EmployeeService
from src.services.rent_agreement_service import RentAgreementService
from src.services.tool_service import ToolService
from src.view.add_rent_agreement_view import AddRentAgreementView
from src.view.adapters import ClientAdapter, EmployeeAdapter, ToolAdapter


class AddRentAgreementController:
    def __init__(self, view, main_controller, client_service: ClientService, tool_service: ToolService, employee_service: EmployeeService, rent_agreement_service: RentAgreementService):
        self.main_controller = main_controller
        self.view: AddRentAgreementView = view
        self.client_service = client_service
        self.tool_service = tool_service
        self.employee_service = employee_service
        self.rent_agreement_service = rent_agreement_service

        # Заполняем комбобоксы данными с использованием адаптеров
        self.populate_comboboxes()

        # Подключаем кнопку
        self.view.submit_button.clicked.connect(self.add_rent_agreement)
        self.view.rejected.connect(self.on_close)
        self.view.accepted.connect(self.on_close)

    def show_window(self):
        self.view.exec()

    def populate_comboboxes(self):
        """Заполняет комбобоксы данными с использованием адаптеров."""
        # Клиенты
        clients = self.client_service.get_client_list()
        for client in clients:
            adapter = ClientAdapter(client)
            self.view.client_combo.addItem(adapter.text(), client.passport)  # Используем passport как данные

        # Инструменты
        tools = self.tool_service.get_tool_list()
        for tool in tools:
            adapter = ToolAdapter(tool)
            self.view.tool_combo.addItem(adapter.text(), tool.name)  # Используем name как данные

        # Сотрудники
        employees = self.employee_service.get_employee_list()
        for employee in employees:
            adapter = EmployeeAdapter(employee)
            self.view.employee_combo.addItem(adapter.text(), employee.id)  # Используем id как данные

    def add_rent_agreement(self):
        try:
            # Получаем данные из формы
            client_passport = self.view.client_combo.currentData()  # Получаем passport клиента
            tool_name = self.view.tool_combo.currentData()  # Получаем name инструмента
            employee_id = self.view.employee_combo.currentData()  # Получаем id сотрудника
            days = int(self.view.days_input.text())

            # Добавляем договор аренды
            self.rent_agreement_service.add_rent_agreement(
                days=days,
                tool_name=tool_name,
                employee_id=employee_id,
                client_passport=client_passport
            )

            # Закрываем окно и включаем главное окно
            self.view.close()
            self.main_controller.enable_window()
        except Exception as e:
            print(f"Ошибка: {e}")

    def on_close(self):
        """Метод, вызываемый при закрытии окна."""
        self.main_controller.enable_window()  # Разблокируем основное окно