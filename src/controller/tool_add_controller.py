from src.view.tool_add_dialog_view import ToolAddView
from src.services.tool_service import ToolService


class ToolAddController:
    def __init__(self, view, main_controller, tool_service: ToolService):
        self.main_controller = main_controller
        self.view: ToolAddView = view
        self.tool_service = tool_service
        self.view.rejected.connect(self.open_main_window)
        # self.view.ui.buttonBox.accepted.connect(self.save_client)
        self.view.accept = self.save_client

    def show_tool_window(self):
        self.view.exec()

    def save_client(self):
        print("save")
        name = self.view.ui.name.text()
        category = self.view.ui.category.text()
        rent_cost = int(self.view.ui.cost.text())
        amount = int(self.view.ui.amount.text())
        try:
            self.tool_service.add_tool(name, category, rent_cost, amount)
        except Exception as ex:
            print(ex)
            return
        self.view.close()
        self.main_controller.enable_window()

    def open_main_window(self):
        self.main_controller.enable_window()
