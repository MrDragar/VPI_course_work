from src.services.employee_service import EmployeeService
from src.view.employee_list_view import EmployeeListView
from src.view.adapters import EmployeeAdapter


class EmployeeListController:
    def __init__(self, view, main_controller, employee_service: EmployeeService):
        self.main_controller = main_controller
        self.view: EmployeeListView = view
        self.employee_service = employee_service

        # Заполняем список сотрудников
        self.populate_list()

        # Подключаем сигналы закрытия окна
        self.view.rejected.connect(self.on_close)
        self.view.accepted.connect(self.on_close)

    def show_window(self):
        self.view.exec()

    def populate_list(self):
        """Заполняет список сотрудников."""
        employees = self.employee_service.get_employee_list()
        for employee in employees:
            adapter = EmployeeAdapter(employee)
            self.view.list_widget.addItem(adapter)

    def on_close(self):
        """Метод, вызываемый при закрытии окна."""
        self.main_controller.enable_window()  # Разблокируем основное окно
