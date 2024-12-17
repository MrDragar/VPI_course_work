from src.services.rent_agreement_service import RentAgreementService
from src.view.agreements_view import AgreementsView


class AgreementsController:
    def __init__(self, view, main_controller, rent_agreement_service: RentAgreementService):
        self.main_controller = main_controller
        self.view: AgreementsView = view
        self.rent_agreement_service = rent_agreement_service

        agreements = self.rent_agreement_service.get_rent_agreement_list()
        for agreement in agreements:
            self.view.list_widget.addItem(f"Договор {agreement.id}: {agreement.tool} - {agreement.status}")

        self.view.rejected.connect(self.on_close)
        self.view.accepted.connect(self.on_close)

    def show_window(self):
        self.view.exec()

    def on_close(self):
        """Метод, вызываемый при закрытии окна."""
        self.main_controller.enable_window()  # Разблокируем основное окно
