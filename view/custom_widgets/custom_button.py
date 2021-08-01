import sys

from PySide6.QtGui import QColor, QPaintEvent, QPainter, Qt
from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow, QFrame, QGridLayout


class CustomButton(QPushButton):

    def __init__(self):
        super().__init__()
        self._background_color = QColor(255, 255, 255)
        self._border_color = QColor(20, 130, 0)
        self._selected_color = self._border_color
        self.setCheckable(True)
        self.setText("Este es un boton de prueba")
        self.setObjectName("UA_button")
        self.clicked.connect(self.change_size)

    def change_size(self) -> None:
        if self.isChecked():
            self.setFixedHeight(150)
            self.setText(self.text() + "\nEste es un texto agregado \n kncfvifcas")
        else:
            self.setFixedHeight(50)
            self.setText("Otro texto")


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)

        # CREATE CONTAINER AND LAYOUT
        self.container = QFrame()
        self.container.setObjectName("container")
        self.container.setStyleSheet("#container { background-color: #222 }")
        self.layout = QGridLayout()

        # ADD WIDGETS TO LAYOUT
        self.toogle = CustomButton()

        self.layout.addWidget(self.toogle, Qt.AlignCenter, Qt.AlignCenter)

        # SET CENTRAL WIDGET
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        # SHOW WINDOW
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
