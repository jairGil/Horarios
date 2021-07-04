class Hora:
    _hora: int
    _minuto: int

    def __init__(self, hora: int, minuto: int) -> None:
        self.set_hora(hora)
        self.set_minuto(minuto)

    def get_hora(self) -> int:
        return self._hora

    def set_hora(self, hora: int) -> None:
        if 0 < hora < 24:
            self._hora = hora
        else:
            self._hora = 0
    
    def get_minuto(self) -> int:
        return self._minuto

    def set_minuto(self, minuto: int) -> None:
        if 0 < minuto < 60:
            self._minuto = minuto
        else:
            self._minuto = 0

    def compara_hora(self, hora: "Hora") -> int:
        horas = hora.get_hora() - self._hora
        minutos = hora.get_minuto() - self._minuto
        return horas * 60 + minutos

    def __str__(self) -> str:
        return f"{self._hora}:{self._minuto}"
