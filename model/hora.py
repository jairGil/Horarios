from typing import Any


class Hora:
    _hora: int
    _minuto: int

    def __init__(self, hora: int, minuto: int) -> None:
        self._hora = hora
        self._minuto = minuto

    def get_hora(self) -> int:
        return self._hora

    def set_hora(self, hora: int) -> None:
        if hora > 0 and hora < 24:
            self._hora = hora
        else:
            self._hora = 0
    
    def get_minuto(self) -> int:
        return self._minuto

    def set_minuto(self, minuto: int) -> None:
        if minuto > 0 and minuto < 60:
            self._minuto = minuto
        else:
            self._minuto = 0

    def compara_hora(self, hora) -> int:
        if hora.get_hora() - self._hora == 0 and hora.get_minuto() - self._minuto == 0:
            return 0
        else:
            return 1

    def __str__(self) -> str:
        return f"{self._hora}:{self._minuto}"