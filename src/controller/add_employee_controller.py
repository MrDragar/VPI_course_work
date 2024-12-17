from src.services.employee_service import EmployeeService
from src.view.add_employee_view import AddEmployeeView


class AddEmployeeController:
    def __init__(self, view, main_controller,
                 employee_service: EmployeeService):
        self.main_controller = main_controller
        self.view: AddEmployeeView = view
        self.employee_service = employee_service

        # Подключаем кнопку
        self.view.submit_button.clicked.connect(self.add_employee)

        # Подключаем сигналы закрытия окна
        self.view.rejected.connect(self.on_close)
        self.view.accepted.connect(self.on_close)

    def show_window(self):
        self.view.exec()

    def add_employee(self):
        try:
            # Получаем данные из формы
            fio = self.view.fio_input.text()
            phone = self.view.phone_input.text()
            email = self.view.email_input.text()
            birthday = self.view.birthday_input.date().toPython()

            # Добавляем сотрудника
            self.employee_service.add_employee(fio, phone, email, birthday)

            # Закрываем окно
            self.view.close()

        except Exception as e:
            print(f"Ошибка: {e}")

    def on_close(self):
        """Метод, вызываемый при закрытии окна."""
        self.main_controller.enable_window()  # Разблокируем основное окно
