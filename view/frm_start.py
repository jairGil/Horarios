from PySide6 import QtWidgets, QtCore


class FrmStart(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()

        # Widget declaration
        self.grid_extern = QtWidgets.QGridLayout(self)
        self.frm_buttons = QtWidgets.QFrame(self)
        self.grid_buttons = QtWidgets.QGridLayout(self.frm_buttons)
        self.lbl_fiuaemex = QtWidgets.QLabel(self.frm_buttons)
        self.btn_ici = QtWidgets.QPushButton(self.frm_buttons)
        self.btn_ico = QtWidgets.QPushButton(self.frm_buttons)
        self.btn_iel = QtWidgets.QPushButton(self.frm_buttons)
        self.btn_ime = QtWidgets.QPushButton(self.frm_buttons)
        self.btn_ises = QtWidgets.QPushButton(self.frm_buttons)

        # Spacer declaration
        self.spacerh = QtWidgets.QSpacerItem(0, 20, hData=QtWidgets.QSizePolicy.Expanding)
        self.spacerh_2 = QtWidgets.QSpacerItem(0, 20, hData=QtWidgets.QSizePolicy.Expanding)
        self.spacerh_3 = QtWidgets.QSpacerItem(40, 20, hData=QtWidgets.QSizePolicy.Expanding)
        self.spacerh_4 = QtWidgets.QSpacerItem(40, 20, hData=QtWidgets.QSizePolicy.Expanding)
        self.spacerv = QtWidgets.QSpacerItem(20, 0, vData=QtWidgets.QSizePolicy.Expanding)
        self.spacerv_2 = QtWidgets.QSpacerItem(20, 0, vData=QtWidgets.QSizePolicy.Expanding)

        self.setup_ui()

    def setup_ui(self) -> None:

        # Set Minimum Sizes
        self.frm_buttons.setMinimumSize(QtCore.QSize(400, 0))
        self.lbl_fiuaemex.setMinimumSize(QtCore.QSize(0, 200))
        self.lbl_fiuaemex.setObjectName("lbl_fiuaemex")

        # Place Widgets
        self.grid_buttons.addWidget(self.btn_ici, 0, 1)
        self.grid_buttons.addWidget(self.btn_ico, 1, 1)
        self.grid_buttons.addWidget(self.btn_iel, 2, 1)
        self.grid_buttons.addWidget(self.btn_ime, 3, 1)
        self.grid_buttons.addWidget(self.btn_ises, 4, 1)
        self.grid_buttons.addItem(self.spacerh_3, 0, 0)  # Left Spacer
        self.grid_buttons.addItem(self.spacerh_4, 0, 2)  # Rigth Spacer

        self.grid_extern.addItem(self.spacerh, 2, 0)  # Left Spacer
        self.grid_extern.addItem(self.spacerv, 3, 1)  # Bottom Spacer
        self.grid_extern.addItem(self.spacerh_2, 2, 2)  # Rigth Spacer
        self.grid_extern.addItem(self.spacerv_2, 0, 1)  # Top Spacer
        self.grid_extern.addWidget(self.lbl_fiuaemex, 1, 1)  # Icon Label
        self.grid_extern.addWidget(self.frm_buttons, 2, 1)  # Button´s Frame

        self.retranslate_ui()

    def retranslate_ui(self) -> None:
        # Widgets text's
        self.lbl_fiuaemex.setText("")
        self.btn_ici.setText("ICI")
        self.btn_ico.setText("ICO")
        self.btn_iel.setText("IEL")
        self.btn_ime.setText("IME")
        self.btn_ises.setText("ISES")
