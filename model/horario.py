from hora import Hora


class Horario:
    __horario: list

    def __init__(self):
        self.__horario = []

    def inserta_clase(self, dia: str, hora_inicio: Hora, hora_fin: Hora):
        self.__horario.append({
            "dia": dia,
            "inicio": hora_inicio,
            "fin": hora_fin
        })

    def __str__(self):
        txt = ""
        for h in self.__horario:
            txt += f"{h['dia']} : {h['inicio']} - {h['fin']}\n"
        return txt
