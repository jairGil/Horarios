from PySide6 import QtWidgets


class FrmTemplate(QtWidgets.QFrame):

    def __init__(self):
        super().__init__()

        # Widgets
        self.page_template_layout = QtWidgets.QVBoxLayout(self)
        self.tableWidget = QtWidgets.QTableWidget(self)

        self.setup_ui()

    def setup_ui(self) -> None:
        self.page_template_layout.addWidget(self.tableWidget)
