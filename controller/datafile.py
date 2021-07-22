class DataFile:
    __text: list
    __data: list
    __sched: list
    __uas: set

    def __init__(self):
        self.__data = []
        self.__uas = set()
        self.__sched = []

    def open(self, ruta: str) -> None:
        file = open(ruta, "r")
        self.__text = file.readlines()
        file.close()

        for i in range(len(self.__text)):
            self.__text[i] = self.__text[i].replace("\n", "")

    def _search_scheds(self) -> None:
        for i in range(int(len(self.__text) / 25)):
            self.__sched.append(self.__text[25 * i: (25 * (i + 1))])

    def _search_uas(self) -> None:
        for ua in self.__sched:
            self.__uas.add(ua[3])

    def get_text(self) -> list:
        return self.__text

    def get_sched(self) -> list:
        if self.__sched.__len__() == 0:
            self._search_scheds()
        return self.__sched

    def get_uas(self) -> set:
        if self.__uas.__len__() == 0:
            self._search_uas()
        return self.__uas

    def get_num_uas(self):
        if self.__uas.__len__() == 0:
            self._search_scheds()
            self._search_uas()
        return len(self.__uas)


if __name__ == "__main__":
    fichero = DataFile()
    fichero.open("../controller/templates/PLANTILLA_ICO_2021B.txt")
    materias = fichero.get_sched()

    uas = fichero.get_uas()

    for m in materias:
        print(m)

    print(fichero.get_num_uas())
