import PySide6.QtWidgets

from src.model.tool import Tool
from src.view.tool_list_view import ToolListView
from src.services.tool_service import ToolService


class ToolAdapter(PySide6.QtWidgets.QListWidgetItem):
    def __init__(self, tool: Tool):
        super().__init__()
        self.tool = tool
        self.setText(str(tool))


class ToolListController:
    def __init__(self, view, main_controller, tool_service: ToolService):
        self.main_controller = main_controller
        self.view: ToolListView = view
        self.tool_service = tool_service
        self.view.accepted.connect(self.open_main_window)
        self.view.rejected.connect(self.open_main_window)

    def show_tool_window(self):
        tools = self.tool_service.get_tool_list()

        for tool in tools:
            self.view.ui.listWidget.addItem(ToolAdapter(tool))
        self.view.exec()

    def open_main_window(self):
        self.main_controller.enable_window()
