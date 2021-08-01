from PySide6 import QtWidgets

from view import stylesheets
from view.frm_info import FrmInfo
from view.frm_left_panel import FrmLeftPanel
from view.frm_schedule import FrmSchedule
from view.frm_template import FrmTemplate
from view.frm_ua import FrmUA


class FrmApp(QtWidgets.QFrame):

    def __init__(self):
        super().__init__()
        self.main_layout_h = QtWidgets.QHBoxLayout(self)  # Principal layout

        self.frm_buttons = FrmLeftPanel()  # Left side widgets
        self.stack_pages = QtWidgets.QStackedWidget(self)  # Right side widgets

        self.page_ua = FrmUA()  # First Page
        self.page_template = FrmTemplate()  # Second Page
        self.page_schedule = FrmSchedule()  # Third Page
        self.page_info = FrmInfo()  # Fourth page

        self.setup_ui()

    def setup_ui(self) -> None:
        self.setStyleSheet(stylesheets.style_second)
        # Principal layout config
        self.main_layout_h.setContentsMargins(0, 0, 0, 0)
        # ----------------------Left Panel-------------------------- #
        # Add left frame to window
        self.main_layout_h.addWidget(self.frm_buttons)
        self.set_actions()
        # ----------------------Right Panel------------------------- #
        # ----------------------Page One
        self.stack_pages.addWidget(self.page_ua)
        # self.__placer.place_checkboxes(self.checkboxes_uas, self.ua_layout)
        # ----------------------Page Two
        self.stack_pages.addWidget(self.page_template)
        # ----------------------Page Three
        self.stack_pages.addWidget(self.page_schedule)
        # ----------------------Page Fourth
        self.stack_pages.addWidget(self.page_info)
        # ----------------------Add Stacked Widget to window---------------------- #
        self.main_layout_h.addWidget(self.stack_pages)

        self.retranslate_ui()

    def retranslate_ui(self) -> None:
        self.setWindowTitle("Creacion de Horarios FIUAEMex")

    def set_actions(self) -> None:
        self.frm_buttons.btn_ua.clicked.connect(self.change_pages)
        self.frm_buttons.btn_template.clicked.connect(self.change_pages)
        self.frm_buttons.btn_sched.clicked.connect(self.change_pages)
        self.frm_buttons.btn_info.clicked.connect(self.change_pages)

    def change_pages(self) -> None:
        if self.frm_buttons.btn_ua.isChecked():
            self.stack_pages.setCurrentIndex(0)
        if self.frm_buttons.btn_template.isChecked():
            self.stack_pages.setCurrentIndex(1)
        if self.frm_buttons.btn_sched.isChecked():
            self.stack_pages.setCurrentIndex(2)
        if self.frm_buttons.btn_info.isChecked():
            self.stack_pages.setCurrentIndex(3)
