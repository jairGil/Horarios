import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QStackedWidget, QApplication

from view.frm_app import FrmApp
from view.frm_start import FrmStart
import stylesheets


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 500)
        self.setWindowIcon(QIcon("../view/images/uaemex.png"))
        self.setWindowTitle("Creador de Horarios FIUAEMex")
        self.setStyleSheet(stylesheets.style_first)

        # Stacked widget central_widget
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        # Frame first page
        self.frm_start = FrmStart()
        self.central_widget.addWidget(self.frm_start)

        # Frame second page
        self.frm_app = FrmApp()
        self.central_widget.addWidget(self.frm_app)

        self.central_widget.setCurrentIndex(0)

        self.set_actions()

        # SHOW WINDOW
        self.show()

    def set_actions(self):
        self.frm_start.btn_ico.clicked.connect(lambda: self.central_widget.setCurrentIndex(1))
        self.frm_app.frm_buttons.btn_exit.clicked.connect(lambda: self.central_widget.setCurrentIndex(0))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec())
