class Archivo:
    __contenido: list
    __materias: list
    __uas: set

    def __init__(self):
        self.__datos = []
        self.__uas = set()
        self.__materias = []

    def abrir(self, ruta: str) -> None:
        arch = open(ruta, "r")
        self.__contenido = arch.readlines()
        arch.close()

        self.__contenido = self.__contenido[58:]

        for i in range(len(self.__contenido)):
            self.__contenido[i] = self.__contenido[i].replace("\n", "")

    def buscar_materias(self) -> None:
        for i in range(int(len(self.__contenido) / 25)):
            self.__materias.append(self.__contenido[25 * i: (25 * (i + 1))])

    def buscar_uas(self) -> None:
        for ua in self.__materias:
            self.__uas.add(ua[3])

    def obtener_contenido(self) -> list:
        return self.__contenido

    def obtener_materias(self) -> list:
        return self.__materias

    def obtener_uas(self) -> set:
        return self.__uas


if __name__ == "__main__":
    fichero = Archivo()
    fichero.abrir("PLANTILLA_ICO_2021B.txt")
    fichero.buscar_materias()
    materias = fichero.obtener_materias()

    fichero.buscar_uas()
    uas = fichero.obtener_uas()

    for m in materias:
        print(m)

    print(len(uas))
