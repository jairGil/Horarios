from PyQt5 import QtWidgets

from view.v1 import VentanaPrincipal

if __name__ == "__main__":
    import sys
    from controller.leer_txt import Data
    data = Data("ICO.txt")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = VentanaPrincipal(MainWindow, data)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
