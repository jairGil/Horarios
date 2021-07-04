from hora import Hora


class Horario:
    _horario: list

    def __init__(self):
        self._horario = []

    def inserta_clase(self, dia: str, hora_inicio: Hora, hora_fin: Hora):
        self._horario.append({
            "dia": dia,
            "inicio": hora_inicio,
            "fin": hora_fin
        })

    def __str__(self):
        txt = ""
        for h in self._horario:
            txt += f"{h['dia']} : {h['inicio']} - {h['fin']}\n"
        return txt
