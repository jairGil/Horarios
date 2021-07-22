from PySide6 import QtCore, QtWidgets

from controller.datafile import DataFile
from view import stylesheets


class FrmApp(object):
    __window: QtWidgets.QMainWindow
    __controller: DataFile

    def __init__(self, form: QtWidgets.QWidget, window: QtWidgets.QMainWindow, controller: DataFile):
        # Init controller
        self.__window = window
        self.__controller = controller

        self.main_layout_h = QtWidgets.QHBoxLayout(form)  # Principal layout

        # Left side widgets
        self.frm_buttons = QtWidgets.QFrame(form)
        self.left_buttons_layout = QtWidgets.QVBoxLayout(self.frm_buttons)
        self.btn_ua = QtWidgets.QPushButton(self.frm_buttons)
        self.btn_template = QtWidgets.QPushButton(self.frm_buttons)
        self.btn_sched = QtWidgets.QPushButton(self.frm_buttons)
        self.spacer_item = QtWidgets.QSpacerItem(20, 40, vData=QtWidgets.QSizePolicy.Expanding)
        self.btn_info = QtWidgets.QPushButton(self.frm_buttons)
        self.btn_exit = QtWidgets.QPushButton(self.frm_buttons)

        # Right side widgets
        self.stack_pages = QtWidgets.QStackedWidget(form)  # Stacked widget for multiple Frames

        # First Page
        self.page_ua = QtWidgets.QWidget()
        self.grid_ua = QtWidgets.QGridLayout(self.page_ua)
        self.scrollArea = QtWidgets.QScrollArea(self.page_ua)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scroll_area_layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.frm_ua = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.ua_layout = QtWidgets.QVBoxLayout(self.frm_ua)
        self.checkboxes_uas = []
        self.spacer_item_1 = QtWidgets.QSpacerItem(371, 20, hData=QtWidgets.QSizePolicy.Expanding)
        self.btn_save = QtWidgets.QPushButton(self.page_ua)

        # Second Page
        self.page_template = QtWidgets.QWidget()
        self.page_template_layout = QtWidgets.QVBoxLayout(self.page_template)
        self.tableWidget = QtWidgets.QTableWidget(self.page_template)

        # Third Page
        self.page_schedule = QtWidgets.QWidget()

        # Fourth page
        self.page_info = QtWidgets.QWidget()
        self.page_info_layout = QtWidgets.QVBoxLayout(self.page_info)
        self.lbl_info = QtWidgets.QLabel(self.page_info)

        self.setup_ui(form)

    def setup_ui(self, form):
        form.setStyleSheet(stylesheets.style_second)

        # Principal layout config
        self.main_layout_h.setContentsMargins(0, 0, 0, 0)
        self.main_layout_h.setSpacing(0)

        # ----------------------Left Panel-------------------------- #
        # Fame size and layout
        self.frm_buttons.setMinimumSize(QtCore.QSize(200, 0))
        self.frm_buttons.setObjectName("frm_buttons")
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

        # Add button's action
        self.btn_ua.clicked.connect(self.change_pages)
        self.btn_template.clicked.connect(self.change_pages)
        self.btn_sched.clicked.connect(self.change_pages)
        self.btn_info.clicked.connect(self.change_pages)

        # Add left frame to window
        self.main_layout_h.addWidget(self.frm_buttons)

        # ----------------------Right Panel------------------------- #
        # Set style QPushButtons
        self.stack_pages.setStyleSheet("QPushButton{\n"
                                       "    border-radius: 10px;\n"
                                       "    height: 30;\n"
                                       "    font: 10pt;\n"
                                       "}")

        # ----------------------Page One
        self.grid_ua.setSpacing(9)  # Grid Layout

        # Scroll area porpreties
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 483, 431))
        self.scroll_area_layout.setContentsMargins(0, 0, 0, 0)
        self.ua_layout.setContentsMargins(8, 8, 8, 8)

        # Add widgets to Page One
        self.scroll_area_layout.addWidget(self.frm_ua)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.grid_ua.addWidget(self.scrollArea, 0, 0, 1, 2)
        self.grid_ua.addItem(self.spacer_item_1, 1, 0, 1, 1)
        self.btn_save.setMinimumSize(QtCore.QSize(100, 0))
        self.grid_ua.addWidget(self.btn_save, 1, 1, 1, 1)
        self.stack_pages.addWidget(self.page_ua)

        # ----------------------Page Two
        self.stack_pages.addWidget(self.page_template)
        self.page_template_layout.addWidget(self.tableWidget)

        # ----------------------Page Two
        self.stack_pages.addWidget(self.page_schedule)

        # ----------------------Page Fourth
        self.stack_pages.addWidget(self.page_info)
        self.lbl_info.setAlignment(QtCore.Qt.AlignCenter)
        self.page_info_layout.addWidget(self.lbl_info)

        # ----------------------Add Stacked Widget to window---------------------- #
        self.main_layout_h.addWidget(self.stack_pages)

        self.retranslate_ui(form)
        self.stack_pages.setCurrentIndex(4)

        self.place_checboxes()

    def retranslate_ui(self, form):
        form.setWindowTitle("Creacion de Horarios FIUAEMex")
        self.btn_ua.setText("UA")
        self.btn_template.setText("Plantilla")
        self.btn_sched.setText("Horarios")
        self.btn_info.setText("Acerca de")
        self.btn_exit.setText("Salir")
        self.btn_save.setText("Guardar")
        self.lbl_info.setText("Panel de informacion\n V1")

    def place_checboxes(self):
        uas = self.__controller.get_uas()
        uas = list(uas)
        uas.sort()

        for i in range(len(uas)):
            self.checkboxes_uas.append(QtWidgets.QCheckBox(self.frm_ua))
            self.checkboxes_uas[i].setText(uas[i])
            self.ua_layout.addWidget(self.checkboxes_uas[i])

    def change_pages(self):
        if self.btn_ua.isChecked():
            self.stack_pages.setCurrentIndex(0)
        if self.btn_template.isChecked():
            self.stack_pages.setCurrentIndex(1)
        if self.btn_sched.isChecked():
            self.stack_pages.setCurrentIndex(2)
        if self.btn_info.isChecked():
            self.stack_pages.setCurrentIndex(3)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = FrmApp(Form)
    ui.setup_ui(Form)
    Form.show()
    sys.exit(app.exec())
