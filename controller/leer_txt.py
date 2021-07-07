class Data:
    def __init__(self, name):
        self.__arch = open(name, "r", encoding="UTF-8")
        self.__data = self.__arch.readlines()
        self.__arch.close()

    def get_data(self) -> list:
        data = []
        for line in self.__data:
            data.append(line.replace("\n", "").split(", "))
        return data


if __name__ == '__main__':
    '''
    arch = open("ICO.txt", "r", encoding="UTF-8")
    datos = arch.readlines()
    arch.close()

    print(f"{'Estudios':<15} {'Profesor':<40} {'Clave':<20} {'Materia':<50} {'Tipo':<25} {'Modalidad':<20} {'Grupo':<8}"
          f"{'Lunes':<20} {'Martes':<20} {'Miercoles':<20} {'Jueves':<20} {'Viernes':<20} {'Sabado':<20}")

    for item in datos:
        try:
            item = item.replace("\n", "")
            linea = item.split(", ")
            txt = f'{linea[0]:<15} {linea[1]:<40} {linea[2]:<20} {linea[3]:<50} {linea[4]:<25} {linea[5]:<20} ' \
                  f'{linea[6]:<8} {linea[7]:<20} {linea[8]:<20} {linea[9]:<20} {linea[10]:<20} {linea[11]:<20} ' \
                  f'{linea[12]:<20}'
            print(txt)
        except IndexError:
            print()
        '''

