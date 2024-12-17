from PySide6.QtWidgets import QListWidgetItem
from src.model import Client, Employee, Tool, RentAgreement


class ClientAdapter(QListWidgetItem):
    def __init__(self, client: Client):
        super().__init__()
        self.client = client
        self.setText(f"{client.FIO} ({client.passport})")


class EmployeeAdapter(QListWidgetItem):
    def __init__(self, employee: Employee):
        super().__init__()
        self.employee = employee
        self.setText(f"{employee.FIO} ({employee.id})")


class ToolAdapter(QListWidgetItem):
    def __init__(self, tool: Tool):
        super().__init__()
        self.tool = tool
        self.setText(f"{tool.name} ({tool.category})")


class RentAgreementAdapter(QListWidgetItem):
    def __init__(self, agreement: RentAgreement):
        super().__init__()
        self.agreement = agreement
        self.setText(
            f"Договор {agreement.id}: {agreement.tool} - {agreement.status}"
        )
