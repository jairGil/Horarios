from PySide6 import QtCore, QtGui, QtWidgets


class FrmMain(object):
    def __init__(self, form):
        self.horizontalLayout = QtWidgets.QHBoxLayout(form)
        self.frm_buttons = QtWidgets.QFrame(form)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frm_buttons)
        self.btn_ua = QtWidgets.QPushButton(self.frm_buttons)
        self.btn_template = QtWidgets.QPushButton(self.frm_buttons)
        self.btn_sched = QtWidgets.QPushButton(self.frm_buttons)
        self.btn_info = QtWidgets.QPushButton(self.frm_buttons)
        self.btn_exit = QtWidgets.QPushButton(self.frm_buttons)
        self.stack_pages = QtWidgets.QStackedWidget(form)
        self.page_ua = QtWidgets.QWidget()
        self.gridLayout = QtWidgets.QGridLayout(self.page_ua)
        self.scrollArea = QtWidgets.QScrollArea(self.page_ua)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.btn_save = QtWidgets.QPushButton(self.page_ua)
        self.page_template = QtWidgets.QWidget()
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_template)
        self.tableWidget = QtWidgets.QTableWidget(self.page_template)
        self.page_schedule = QtWidgets.QWidget()
        self.page_info = QtWidgets.QWidget()
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_info)
        self.lbl_info = QtWidgets.QLabel(self.page_info)

    def setup_ui(self, form):
        form.resize(701, 488)
        form.setStyleSheet("QWidget#form{ background-color: rgb(255, 255, 255); }\n"
                           "QFrame{ background-color: rgb(255, 255, 255); }\n"
                           "QFrame#frm_buttons{ background-color: rgb(49, 68, 47); }\n"
                           "QPushButton{\n"
                           "    background-color: rgb(49, 68, 47);\n"
                           "    border: none;\n"
                           "    border-radius: 0px;"
                           "    font: 87 12pt \"Arial Black\";\n"
                           "    color: white;\n"
                           "    height: 50px;\n"
                           "}\n"
                           "QPushButton:hover, QPushButton:checked{ background-color: rgb(167, 150, 77); }\n"
                           "QCheckBox::indicator{\n"
                           "    border: 2px solid;\n"
                           "    border-color: rgb(49, 68, 47);\n"
                           "    width: 15px;\n"
                           "    height: 15px;\n"
                           "    border-radius: 6px;\n"
                           "}\n"
                           "QCheckBox::indicator:checked{ image: url(/imagenes/checkmark.png); }\n"
                           "QCheckBox::indicator:hover{ background-color: rgb(49, 68, 47); }\n"
                           "QScrollBar:vertical{\n"
                           "    border: none;\n"
                           "    width: 15px;\n"
                           "    margin: 15px 0;\n"
                           "    background-color: rgb(177, 177, 177);\n"
                           " }\n"
                           "QScrollBar::handle:vertical{\n"
                           "    background-color: rgb(167, 150, 77);\n"
                           "    min-height: 30px;\n"
                           "    border-radius: 7px;\n"
                           " }\n"
                           "QScrollBar::handle:vertical:pressed, \n"
                           "QScrollBar::add-line:vertical:pressed, \n"
                           "QScrollBar::sub-line:vertical:pressed{ background-color: rgb(29, 40, 28); }\n"
                           "QScrollBar::sub-line:vertical{\n"
                           "    border: none;\n"
                           "    height: 15px;\n"
                           "    background-color: rgb(167, 150, 77);\n"
                           "    border-top-right-radius: 7px;\n"
                           "    border-top-left-radius: 7px;\n"
                           "    subcontrol-position: top;\n"
                           "    subcontrol-origin: margin;\n"
                           "    image: url(/imagenes/sort_up.png);\n"
                           "}\n"
                           "QScrollBar::add-line:vertical{\n"
                           "    border: none;\n"
                           "    height: 15px;\n"
                           "    background-color: rgb(167, 150, 77);\n"
                           "    border-bottom-right-radius: 7px;\n"
                           "    border-bottom-left-radius: 7px;\n"
                           "    subcontrol-position: bottom;\n"
                           "    subcontrol-origin: margin;\n"
                           "    image: url(/imagenes/sort_down.png);\n"
                           "}\n"
                           "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{ background: none; }\n"
                           "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{ background: none; }")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frm_buttons.setMinimumSize(QtCore.QSize(200, 0))
        self.frm_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_buttons.setObjectName("frm_buttons")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_ua.setCheckable(True)
        self.btn_ua.setChecked(True)
        self.btn_ua.setAutoExclusive(True)
        self.btn_ua.setObjectName("btn_ua")
        self.verticalLayout.addWidget(self.btn_ua)
        self.btn_template.setCheckable(True)
        self.btn_template.setAutoExclusive(True)
        self.btn_template.setObjectName("btn_template")
        self.verticalLayout.addWidget(self.btn_template)
        self.btn_sched.setCheckable(True)
        self.btn_sched.setAutoExclusive(True)
        self.btn_sched.setObjectName("btn_sched")
        self.verticalLayout.addWidget(self.btn_sched)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btn_info.setCheckable(True)
        self.btn_info.setAutoExclusive(True)
        self.btn_info.setObjectName("btn_info")
        self.verticalLayout.addWidget(self.btn_info)
        self.btn_exit.setObjectName("btn_exit")
        self.verticalLayout.addWidget(self.btn_exit)
        self.horizontalLayout.addWidget(self.frm_buttons)
        self.stack_pages.setStyleSheet("QPushButton{\n"
                                       "    border-radius: 10px;\n"
                                       "    height: 30;\n"
                                       "    font: 10pt;\n"
                                       "}")
        self.stack_pages.setObjectName("stack_pages")
        self.page_ua.setObjectName("page_ua")
        self.gridLayout.setSpacing(9)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 483, 431))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(371, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.btn_save.setMinimumSize(QtCore.QSize(100, 0))
        self.btn_save.setObjectName("btn_save")
        self.gridLayout.addWidget(self.btn_save, 1, 1, 1, 1)
        self.stack_pages.addWidget(self.page_ua)
        self.page_template.setObjectName("page_template")
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stack_pages.addWidget(self.page_info)
        self.horizontalLayout.addWidget(self.stack_pages)

        self.retranslate_ui(form)
        self.stack_pages.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslate_ui(self, form):
        form.setWindowTitle("Creacion de Horarios FIUAEMex")
        self.btn_ua.setText("UA")
        self.btn_template.setText("Plantilla")
        self.btn_sched.setText("Horarios")
        self.btn_info.setText("Acerca de")
        self.btn_exit.setText("Salir")
        self.btn_save.setText("Guardar")
        self.lbl_info.setText("Panel de informacion\n V1")


# import recursos_rc


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = FrmMain(Form)
    ui.setup_ui(Form)
    Form.show()
    sys.exit(app.exec())
