from PySide6 import QtWidgets


class FrmLeftPanel(QtWidgets.QFrame):

    def __init__(self):
        super().__init__()

        # WIDGETS
        self.left_buttons_layout = QtWidgets.QVBoxLayout(self)
        self.btn_ua = QtWidgets.QPushButton(self)
        self.btn_template = QtWidgets.QPushButton(self)
        self.btn_sched = QtWidgets.QPushButton(self)
        self.spacer_item = QtWidgets.QSpacerItem(20, 40, vData=QtWidgets.QSizePolicy.Expanding)
        self.btn_info = QtWidgets.QPushButton(self)
        self.btn_exit = QtWidgets.QPushButton(self)

        self.setup_ui()

    def setup_ui(self) -> None:
        # Fame size and layout
        self.setMinimumSize(200, 0)
        self.setObjectName("frm_buttons")
        self.left_buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.left_buttons_layout.setSpacing(0)

        # Buttons config
        self.btn_ua.setCheckable(True)
        self.btn_ua.setChecked(True)
        self.btn_ua.setAutoExclusive(True)
        self.btn_template.setCheckable(True)
        self.btn_template.setAutoExclusive(True)
        self.btn_sched.setCheckable(True)
        self.btn_sched.setAutoExclusive(True)
        self.btn_info.setCheckable(True)
        self.btn_info.setAutoExclusive(True)

        # Add Widgets to left panel
        self.left_buttons_layout.addWidget(self.btn_ua)
        self.left_buttons_layout.addWidget(self.btn_template)
        self.left_buttons_layout.addWidget(self.btn_sched)
        self.left_buttons_layout.addItem(self.spacer_item)
        self.left_buttons_layout.addWidget(self.btn_info)
        self.left_buttons_layout.addWidget(self.btn_exit)

        self.retranslate_ui()

    def retranslate_ui(self) -> None:
        self.btn_ua.setText("UA")
        self.btn_template.setText("Plantilla")
        self.btn_sched.setText("Horarios")
        self.btn_info.setText("Acerca de")
        self.btn_exit.setText("Salir")
