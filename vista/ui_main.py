import time

from PySide6 import QtCore, QtWidgets, QtGui

from controlador.archivo import Archivo
from principal import UiMainWindow
from vista.app import FrmMain


class FrmStart:
    __controller: Archivo

    def __init__(self, window: QtWidgets.QMainWindow):
        # Create controller instance
        self.__controller = Archivo()
        self.__window = window

        # Widgets declaration
        self.centralwidget = QtWidgets.QWidget(window)
        self.grd_app = QtWidgets.QGridLayout(self.centralwidget)
        self.lbl_fiuaemex = QtWidgets.QLabel(self.centralwidget)
        self.frm_buttons = QtWidgets.QFrame(self.centralwidget)
        self.grd_frm = QtWidgets.QGridLayout(self.frm_buttons)
        self.btn_ime = QtWidgets.QPushButton(self.frm_buttons)
        self.btn_ises = QtWidgets.QPushButton(self.frm_buttons)
        self.btn_ico = QtWidgets.QPushButton(self.frm_buttons)
        self.btn_iel = QtWidgets.QPushButton(self.frm_buttons)
        self.btn_ici = QtWidgets.QPushButton(self.frm_buttons)

        # Spacers declaration
        self.spacerh = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.spacerh_2 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.spacerh_3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.spacerh_4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.spacerv = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.spacerv_2 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.spacerv_3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.setup_ui(window)

    def setup_ui(self, window: QtWidgets.QMainWindow) -> None:
        window.setCentralWidget(self.centralwidget)
        window.resize(430, 530)
        window.setWindowIcon(QtGui.QIcon("imagenes/uaemex.png"))

        # Look and Feel for GUI
        window.setStyleSheet("QMainWindow{ background-color: rgb(255, 255, 255); }\n"
                             "QPushButton{\n"
                             "	    background-color: rgb(58, 80, 56);\n"
                             "	    border-radius: 20px;\n"
                             "	    font: 18pt \"Algerian\";\n"
                             "	    color: white;\n"
                             "      width: 200;\n"
                             "      height: 40;\n" 
                             "}\n"
                             "QPushButton:hover{ background-color: rgb(167, 150, 77); }\n"
                             "QPushButton:pressed{ background-color: rgb(58, 80, 56); }")

        # Place Widgets and Items in Principal Grid Layout
        self.grd_app.addItem(self.spacerh, 2, 0)  # Left Spacer
        self.grd_app.addItem(self.spacerv, 3, 1)  # Bottom Spacer
        self.grd_app.addItem(self.spacerh_2, 2, 2)  # Rigth Spacer
        self.grd_app.addItem(self.spacerv_2, 0, 1)  # Top Spacer
        self.grd_app.addWidget(self.lbl_fiuaemex, 1, 1)  # Icon Label
        self.grd_app.addWidget(self.frm_buttons, 2, 1)  # Button´s Frame

        # Place Widgets and Items in Frame's Grid Layout
        self.grd_frm.addItem(self.spacerh_3, 0, 0)  # Left Spacer
        self.grd_frm.addItem(self.spacerh_4, 0, 2)  # Rigth Spacer
        self.grd_frm.addItem(self.spacerv_3, 5, 1)  # Bottom Spacer
        self.grd_frm.addWidget(self.btn_ici, 0, 1)
        self.grd_frm.addWidget(self.btn_ico, 1, 1)
        self.grd_frm.addWidget(self.btn_iel, 2, 1)
        self.grd_frm.addWidget(self.btn_ime, 3, 1)
        self.grd_frm.addWidget(self.btn_ises, 4, 1)

        # Set minimum size of label, frame and buttons
        self.lbl_fiuaemex.setMinimumSize(QtCore.QSize(0, 200))
        self.frm_buttons.setMinimumSize(QtCore.QSize(400, 300))
        
        # Add Button's actions
        self.btn_ico.clicked.connect(self.actions)

        # Set icon image in Label
        self.lbl_fiuaemex.setPixmap(QtGui.QPixmap("imagenes/fingenieria.png"))
        self.lbl_fiuaemex.setAlignment(QtCore.Qt.AlignCenter)

        # Retranslate ui
        self.retranslate_ui(window)

    def retranslate_ui(self, window: QtWidgets.QMainWindow) -> None:
        # Set widget's texts
        window.setWindowTitle("Creador de Horarios FIUAEMex")
        self.btn_ico.setText("ICO")
        self.btn_ici.setText("ICI")
        self.btn_iel.setText("IEL")
        self.btn_ime.setText("IME")
        self.btn_ises.setText("ISES")
        self.lbl_fiuaemex.setText("")

    def actions(self):
        """
        self.__controller.abrir("../controlador/plantillas/PLANTILLA_ICO_2021B.txt")
        win2 = QtWidgets.QMainWindow(parent=self.centralwidget)
        second_view = UiMainWindow(self.__controller)
        second_view.setup_ui(win2)
        win2.show()
        MainWindow.hide()
        """
        form = QtWidgets.QWidget()
        ui2 = FrmMain(form)
        ui2.setup_ui(form)
        self.__window.setCentralWidget(form)
        self.__window.showMaximized()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = FrmStart(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
