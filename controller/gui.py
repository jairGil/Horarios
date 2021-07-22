from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtGui import QIcon

from view.main import FrmMain


class MainWin:
    __frm_main: FrmMain
    __window: QMainWindow

    def __init__(self, window: QMainWindow):
        self.centralwidget = QWidget()
        self.__window = window
        self.__frm_main = FrmMain(self.centralwidget, window)

        self.setup_ui()

    def setup_ui(self):
        self.__window.resize(800, 600)
        self.__window.setCentralWidget(self.centralwidget)
        self.__window.setWindowIcon(QIcon("../view/images/uaemex.png"))
        self.__window.setWindowTitle("Creador de Horarios FIUAEMex")
        self.__window.show()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ui = MainWin(QMainWindow())
    sys.exit(app.exec())
