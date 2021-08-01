from PySide6.QtWidgets import QLayout, QCheckBox, QPushButton

from controller.datafile import DataFile
from view.custom_widgets.custom_button import CustomButton


class Placer:
    __controller: DataFile

    def __init__(self, controller: DataFile):
        self.__controller = controller

    def place_checkboxes(self, checkboxes: list, layout: QLayout):
        uas = list(self.__controller.get_uas())
        uas.sort()

        for i in range(len(uas)):
            button = CustomButton()
            button.setCheckable(True)
            checkboxes.append(button)
            layout.addWidget(checkboxes[i])
