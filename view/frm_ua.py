from PySide6 import QtWidgets


class FrmUA(QtWidgets.QFrame):

    def __init__(self):
        super().__init__()

        # First Page
        self.grid_ua = QtWidgets.QGridLayout(self)
        self.lbl_title_page_one = QtWidgets.QLabel(self)
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scroll_area_layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.frm_ua = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.ua_layout = QtWidgets.QVBoxLayout(self.frm_ua)
        self.checkboxes_uas = []
        self.spacer_item_1 = QtWidgets.QSpacerItem(371, 20, hData=QtWidgets.QSizePolicy.Expanding)
        self.btn_save = QtWidgets.QPushButton(self)

        self.setup_ui()

    def setup_ui(self) -> None:
        # Set style QPushButtons
        self.setStyleSheet("QPushButton{\n"
                           "    border-radius: 10px;\n"
                           "    height: 35;\n"
                           "    font: 10pt;\n"
                           "}")

        # ----------------------Page One
        self.grid_ua.setSpacing(9)  # Grid Layout

        # Scroll area porpreties
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents.setGeometry(0, 0, 483, 431)
        self.scroll_area_layout.setContentsMargins(0, 0, 0, 0)
        self.ua_layout.setContentsMargins(8, 8, 8, 8)

        # Add widgets to Page One
        self.scroll_area_layout.addWidget(self.frm_ua)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.grid_ua.addWidget(self.lbl_title_page_one, 0, 0, 1, 2)
        self.grid_ua.addWidget(self.scrollArea, 1, 0, 1, 2)
        self.grid_ua.addItem(self.spacer_item_1, 2, 0, 1, 1)
        self.grid_ua.addWidget(self.btn_save, 2, 1, 1, 1)

        self.retranslate_ui()

    def retranslate_ui(self) -> None:
        self.lbl_title_page_one.setText("Selecciona las materias que ya cursaste")
        self.btn_save.setText("Guardar")
