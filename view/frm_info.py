from PySide6 import QtWidgets, QtCore


class FrmInfo(QtWidgets.QFrame):

    def __init__(self):
        super().__init__()

        # Widgets
        self.page_info_layout = QtWidgets.QVBoxLayout(self)
        self.lbl_info = QtWidgets.QLabel(self)

        self.setup_ui()

    def setup_ui(self) -> None:
        self.lbl_info.setAlignment(QtCore.Qt.AlignCenter)
        self.page_info_layout.addWidget(self.lbl_info)

        self.retranslate_ui()

    def retranslate_ui(self) -> None:
        self.lbl_info.setText("Panel de informacion\n V1")
