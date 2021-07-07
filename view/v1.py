from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from controller.leer_txt import Data


class VentanaPrincipal(object):
    __Titulos = ["GDO.", "NOMBRE", "CLAVE", "MATERIA", "TIPO", "MODALIDAD", "GPO.", "LUNES", "MARTES", "MIERCOLES",
                 "JUEVES", "VIERNES", "SABADO"]

    def __init__(self, MainWin, controlador: Data):
        self.centralwidget = QtWidgets.QWidget(MainWin)
        self.tbl_materias = QtWidgets.QTableWidget(self.centralwidget)
        self.btn_agregar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cargar = QtWidgets.QPushButton(self.centralwidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.__controlador = controlador

    def setupUi(self, MainWin):
        MainWin.resize(717, 534)
        self.verticalLayout.addWidget(self.btn_cargar)
        self.verticalLayout.addWidget(self.btn_agregar)
        spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacer_item)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.tbl_materias.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_materias.setAlternatingRowColors(True)
        self.tbl_materias.setCornerButtonEnabled(False)
        self.tbl_materias.setColumnCount(13)
        self.tbl_materias.setRowCount(0)

        for i in range(13):
            item = QtWidgets.QTableWidgetItem()
            self.tbl_materias.setHorizontalHeaderItem(i, item)

        self.btn_cargar.clicked.connect(self.cargar_tabla)

        self.gridLayout.addWidget(self.tbl_materias, 0, 0, 1, 1)
        MainWin.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWin)
        QtCore.QMetaObject.connectSlotsByName(MainWin)

    def retranslateUi(self, MainWin):
        _translate = QtCore.QCoreApplication.translate
        MainWin.setWindowTitle(_translate("MainWin", "CREADOR DE HORARIOS"))
        self.btn_cargar.setText(_translate("MainWin", "CARGAR"))
        self.btn_agregar.setText(_translate("MainWin", "AGREGAR"))
        self.tbl_materias.setSortingEnabled(True)

        for i in range(13):
            item = self.tbl_materias.horizontalHeaderItem(i)
            item.setText(_translate("MainWin", self.__Titulos[i]))

    def cargar_tabla(self):
        data = self.__controlador.get_data()
        self.tbl_materias.setRowCount(len(data))
        for i in range(len(data)):
            for j in range(len(data[i])):
                item = QTableWidgetItem(data[i][j])
                self.tbl_materias.setItem(i, j, item)
